"""uploaded.json: what has been uploaded, so every command is safe to re-run."""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from .schedule import from_rfc3339


class State:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.data = {"videos": {}, "quota": {}}
        if self.path.is_file():
            self.data = json.loads(self.path.read_text(encoding="utf-8"))
            self.data.setdefault("videos", {}); self.data.setdefault("quota", {})

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.data, indent=2, ensure_ascii=False), encoding="utf-8")
        os.replace(tmp, self.path)

    @staticmethod
    def key(channel: str, item_key: str) -> str:
        return f"{channel}:{item_key}"

    def entry(self, channel: str, item_key: str) -> dict:
        return self.data["videos"].setdefault(self.key(channel, item_key), {"channel": channel, "video": item_key})

    def get(self, channel, item_key):
        return self.data["videos"].get(self.key(channel, item_key))

    def is_done(self, channel, item_key, want_short=True) -> bool:
        e = self.get(channel, item_key) or {}
        long_ok = e.get("long", {}).get("complete")
        short_ok = e.get("short", {}).get("complete") or not want_short or e.get("short", {}).get("skipped")
        return bool(long_ok and short_ok)

    def taken_slots(self, channel: str) -> list[datetime]:
        out = []
        for e in self.data["videos"].values():
            if e.get("channel") != channel:
                continue
            p = e.get("long", {}).get("publishAt")
            if p:
                out.append(from_rfc3339(p))
        return out

    # quota resets at midnight Pacific time
    @staticmethod
    def quota_day() -> str:
        return datetime.now(timezone.utc).astimezone(ZoneInfo("America/Los_Angeles")).date().isoformat()

    def units_used_today(self) -> int:
        return int(self.data["quota"].get(self.quota_day(), 0))

    def add_units(self, n: int):
        d = self.quota_day()
        self.data["quota"] = {d: self.units_used_today() + n}   # keep only today
        self.save()
