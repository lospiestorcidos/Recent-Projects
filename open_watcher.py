#!/usr/bin/env python3
"""Watcher: cuando el dispositivo M4L escribe una peticion en request.txt,
abre ese proyecto en Ableton Live y vacia el fichero.
Uso: python3 open_watcher.py
"""
import json
import os
import subprocess
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REQ = os.path.join(HERE, "request.txt")
APP = "Ableton Live 12 Suite"


def open_project(path):
    subprocess.run(["open", "-a", APP, path], check=False)


def main():
    print("open_watcher: vigilando", REQ)
    last = None
    while True:
        try:
            with open(REQ, "r", encoding="utf-8") as f:
                content = f.read().strip()
        except FileNotFoundError:
            content = ""
        except OSError:
            content = ""
        if content and content != last:
            last = content
            try:
                data = json.loads(content)
                path = data.get("path", content) if isinstance(data, dict) else content
            except ValueError:
                path = content
            if os.path.isfile(path):
                print("Abriendo:", path)
                try:
                    open_project(path)
                except Exception as e:
                    print("Error al abrir:", e)
            else:
                print("No existe el proyecto:", path)
            try:
                with open(REQ, "w", encoding="utf-8") as f:
                    f.write("")
            except OSError:
                pass
        time.sleep(1.0)


if __name__ == "__main__":
    main()
