#!/usr/bin/env python3
"""Entry point:  python yt_upload.py upload <video_folder> --channel happy"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ytup.cli import main
if __name__ == "__main__":
    sys.exit(main())
