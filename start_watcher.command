#!/bin/bash
cd "$(dirname "$0")"
pkill -f open_watcher.py 2>/dev/null
nohup python3 open_watcher.py > watcher.log 2>&1 &
echo "Watcher iniciado (log: watcher.log)"
