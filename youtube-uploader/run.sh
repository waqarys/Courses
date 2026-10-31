#!/usr/bin/env bash
# WSL / Linux / macOS:  ./run.sh upload /mnt/c/working/.../02_Plants --channel happy
cd "$(dirname "$0")"
[ -x .venv/bin/python ] || { python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt; }
exec .venv/bin/python yt_upload.py "$@"
