#!/usr/bin/env python3
"""Escanea los proyectos .als mas recientes y genera:
   - recent.json : [{name, path}] (ordenados por fecha, mas reciente primero)
   - names.txt   : una linea por nombre (para el umenu del dispositivo M4L)
Uso: python3 scan_recent.py [N]
"""
import json
import os
import sys

ROOT = os.path.expanduser("~/Music/Ableton Projects")
HERE = os.path.dirname(os.path.abspath(__file__))


def scan(root, limit):
    res = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        parts = [seg.lower() for seg in dirpath.split(os.sep)]
        if "backup" in parts:
            continue
        for f in files:
            if not f.lower().endswith(".als"):
                continue
            full = os.path.join(dirpath, f)
            try:
                mtime = os.path.getmtime(full)
            except OSError:
                continue
            res.append((mtime, full))
    res.sort(reverse=True)
    return res[:limit]


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    if not os.path.isdir(ROOT):
        print("No existe la carpeta de proyectos:", ROOT)
        sys.exit(1)
    found = scan(ROOT, limit)
    items = [{"name": os.path.splitext(os.path.basename(p))[0], "path": p}
             for _, p in found]
    with open(os.path.join(HERE, "recent.json"), "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=1)
    with open(os.path.join(HERE, "names.txt"), "w", encoding="utf-8") as f:
        for it in items:
            f.write(it["name"] + "\n")
    print("OK %d proyectos -> recent.json / names.txt" % len(items))
    for it in items[:10]:
        print("  %s  (%s)" % (it["name"], os.path.dirname(it["path"])))


if __name__ == "__main__":
    main()
