"""Publish-slot calculation. All slots are local times in the configured timezone."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def parse_days(days) -> set[int]:
    if days in (None, "daily", "everyday", "all"):
        return set(range(7))
    if isinstance(days, str):
        days = [d.strip() for d in days.split(",")]
    return {DAYS.index(d.lower()[:3]) for d in days}


def candidate_slots(sched: dict, start: datetime, horizon_days: int = 120):
    """Yield aware datetimes (in tz) for every configured slot after `start`."""
    tz = ZoneInfo(sched.get("timezone", "Asia/Kolkata"))
    times = sched.get("times", ["07:00"])
    days = parse_days(sched.get("days", "daily"))
    local = start.astimezone(tz)
    for d in range(horizon_days):
        day = (local + timedelta(days=d)).date()
        if day.weekday() not in days:
            continue
        for t in sorted(times):
            hh, mm = map(int, t.split(":"))
            slot = datetime(day.year, day.month, day.day, hh, mm, tzinfo=tz)
            if slot > start:
                yield slot


def next_free_slot(sched: dict, taken: list[datetime], now: datetime | None = None) -> datetime:
    now = now or datetime.now(timezone.utc)
    lead = timedelta(minutes=int(sched.get("min_lead_minutes", 60)))
    taken_utc = {t.astimezone(timezone.utc).replace(second=0, microsecond=0) for t in taken}
    for slot in candidate_slots(sched, now + lead):
        if slot.astimezone(timezone.utc).replace(second=0, microsecond=0) not in taken_utc:
            return slot
    raise RuntimeError("no free slot in the next 120 days - check schedule config")


def short_time(long_slot: datetime, sched: dict) -> datetime:
    return long_slot + timedelta(minutes=int(sched.get("short_offset_minutes", 60)))


def parse_at(value: str, tz_name: str) -> datetime:
    """'2026-11-02 07:00' (local tz) or full ISO with offset."""
    v = value.strip().replace("T", " ")
    try:
        dt = datetime.fromisoformat(v)
    except ValueError:
        raise SystemExit(f"Can't read time '{value}'. Use e.g. \"2026-11-02 07:00\".")
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=ZoneInfo(tz_name))
    return dt


def rfc3339_utc(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")


def from_rfc3339(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))
