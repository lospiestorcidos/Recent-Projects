#!/usr/bin/env python3
"""Genera 'Recent Projects.amxd' (y .maxpat) partiendo de la plantilla
fourin_fourout.amxd de Max 9 (Max Audio Effect valido), reemplazando
los boxes/lines con los de nuestro dispositivo."""
import json
import os
import struct

BASE = "/Users/jorgenavaslosada/Library/Application Support/Cycling '74/Max 9/Examples/resources/fourin_fourout.amxd"
OUT_DIR = os.path.expanduser("~/Documents/AbletonRecent")
os.makedirs(OUT_DIR, exist_ok=True)


def read_patcher(path):
    d = open(path, "rb").read()
    i = d.find(b"ptch")
    length = int.from_bytes(d[i + 4:i + 8], "little")
    obj, _ = json.JSONDecoder().raw_decode(d[i + 8:i + 8 + length].decode("utf-8"))
    return obj["patcher"]


def box(oid, maxclass, text, rect, numinlets=1, numoutlets=1,
        outlettype=None, extra=None):
    b = {
        "id": oid,
        "maxclass": maxclass,
        "patching_rect": rect,
        "style": "",
    }
    if text is not None:
        b["text"] = text
    b["numinlets"] = numinlets
    b["numoutlets"] = numoutlets
    if outlettype is not None:
        b["outlettype"] = outlettype
    if extra:
        b.update(extra)
    return {"box": b}


def main():
    pch = read_patcher(BASE)
    pch["title"] = "Recent Projects"
    pch["description"] = ("Lista los proyectos .als mas recientes y los abre. "
                          "Requiere el watcher open_watcher.py (Documents/AbletonRecent).")

    # conservar solo plugin~/plugout~ (passthrough de audio)
    keep = []
    for b in pch.get("boxes", []):
        t = (b["box"].get("text") or "")
        if t.startswith("plugin~") or t.startswith("plugout~"):
            keep.append(b)
    boxes = keep

    umenu_extra = {
        "parameter_enable": 0,
        "presentation": 1,
        "presentation_rect": [20.0, 40.0, 320.0, 22.0],
        "items": [],
        "fontname": "Arial",
        "fontsize": 11.0,
    }
    btn_style = {"presentation": 1, "presentation_rect": [20.0, 90.0, 150.0, 24.0]}
    btn_style2 = {"presentation": 1, "presentation_rect": [190.0, 90.0, 150.0, 24.0]}

    boxes += [
        box("obj-10", "comment", "Proyectos recientes:", [12.0, 12.0, 320.0, 18.0],
            numinlets=1, numoutlets=0, outlettype=[]),
        box("obj-11", "umenu", None, [20.0, 40.0, 320.0, 22.0],
            numinlets=1, numoutlets=3, outlettype=["int", "", ""], extra=umenu_extra),
        box("obj-12", "newobj", "js recent_loader.js", [30.0, 130.0, 140.0, 20.0],
            numinlets=3, numoutlets=1, outlettype=[""]),
        box("obj-13", "button", None, [20.0, 90.0, 150.0, 24.0],
            numinlets=1, numoutlets=1, outlettype=["bang"], extra=btn_style),
        box("obj-14", "button", None, [190.0, 90.0, 150.0, 24.0],
            numinlets=1, numoutlets=1, outlettype=["bang"], extra=btn_style2),
        box("obj-15", "newobj", "loadbang", [30.0, 160.0, 90.0, 20.0],
            numinlets=0, numoutlets=1, outlettype=["bang"]),
        box("obj-16", "comment", "Abrir (cierra el set actual)", [190.0, 118.0, 180.0, 16.0],
            numinlets=1, numoutlets=0, outlettype=[]),
        box("obj-17", "comment", "Recargar lista", [20.0, 118.0, 120.0, 16.0],
            numinlets=1, numoutlets=0, outlettype=[]),
    ]

    lines = [l for l in pch.get("lines", [])
             if _keep_line(l, keep)]
    lines += [
        line("obj-13", 0, "obj-12", 0),   # Recargar -> js.in0 (bang load)
        line("obj-15", 0, "obj-12", 0),   # loadbang -> js.in0
        line("obj-11", 0, "obj-12", 1),   # umenu.out0 (int) -> js.in1
        line("obj-14", 0, "obj-12", 2),   # Abrir -> js.in2 (bang open)
        line("obj-12", 0, "obj-11", 0),   # js.out0 -> umenu.in0
    ]

    pch["boxes"] = boxes
    pch["lines"] = lines

    payload = json.dumps({"patcher": pch}, indent=1, ensure_ascii=False).encode("utf-8")
    payload += b"\n"

    # .amxd con el contenedor ampf (igual que los ficheros de Max 9)
    amxd = (b"ampf" + struct.pack("<I", 4) + b"aaaa"
            + b"meta" + struct.pack("<I", 4) + b"\x00\x00\x00\x00"
            + b"ptch" + struct.pack("<I", len(payload)) + payload)
    with open(os.path.join(OUT_DIR, "Recent Projects.amxd"), "wb") as f:
        f.write(amxd)

    # .maxpat en texto plano (para abrir/editar en Max)
    with open(os.path.join(OUT_DIR, "Recent Projects.maxpat"), "w", encoding="utf-8") as f:
        json.dump({"patcher": pch}, f, indent=1, ensure_ascii=False)

    print("OK ->", OUT_DIR)


def line(src, out, dst, inn):
    return {"patchline": {"source": [src, out], "destination": [dst, inn]}}


def _keep_line(l, keep):
    ids = {b["box"]["id"] for b in keep}
    pl = l.get("patchline", {})
    return pl.get("source", ["", 0])[0] in ids and pl.get("destination", ["", 0])[0] in ids


if __name__ == "__main__":
    main()
