"""Local-time helpers for clawplay.

Centralizes timezone handling so every timestamp in reports renders in the
viewer's local timezone. Defaults to America/Chicago (CST/CDT — Tyler is
DFW-based). Override with $CLAWPLAY_TZ.

Public surface (unchanged from prior version so old call sites still work):
    local_now(tz=None) -> datetime
    to_local(dt, tz=None) -> datetime
    format_local(dt, fmt=..., tz=None) -> str
    countdown_to_kickoff(kickoff_iso, tz=None) -> str
"""

from __future__ import annotations

import datetime as _dt
import os
from typing import Optional

try:
    from zoneinfo import ZoneInfo  # Python 3.9+
except ImportError:
    ZoneInfo = None  # type: ignore

DEFAULT_TZ = os.environ.get("CLAWPLAY_TZ", os.environ.get("LIVE_SPORTS_TZ", "America/Chicago"))


def local_now(tz: Optional[str] = None) -> _dt.datetime:
    """Return current time in viewer's local timezone (DST-aware)."""
    tz_name = tz or DEFAULT_TZ
    if ZoneInfo is None:
        return _dt.datetime.now()
    try:
        return _dt.datetime.now(ZoneInfo(tz_name))
    except Exception:
        return _dt.datetime.now()


def to_local(dt: _dt.datetime, tz: Optional[str] = None) -> _dt.datetime:
    """Convert a datetime (naive or aware) to viewer's local timezone."""
    tz_name = tz or DEFAULT_TZ
    if ZoneInfo is None:
        return dt
    try:
        target = ZoneInfo(tz_name)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=_dt.timezone.utc)
        return dt.astimezone(target)
    except Exception:
        return dt


def format_local(
    dt: _dt.datetime,
    fmt: str = "%a %b %-d · %-I:%M %p",
    tz: Optional[str] = None,
) -> str:
    """Format a datetime in viewer's local timezone.  e.g. 'Thu Jun 18 · 9:00 PM'."""
    try:
        local = to_local(dt, tz)
        return local.strftime(fmt)
    except Exception:
        return str(dt)


def parse_iso(s: Optional[str]) -> Optional[_dt.datetime]:
    """Parse an ISO-ish datetime string; return aware datetime or None."""
    if not s:
        return None
    try:
        s2 = s.replace("Z", "+00:00")
        dt = _dt.datetime.fromisoformat(s2)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=_dt.timezone.utc)
        return dt
    except Exception:
        return None


def countdown_to_kickoff(kickoff_iso: str, tz: Optional[str] = None) -> str:
    """Compute a human-readable countdown to kickoff.

    Returns:
      - "2d 5h"   when >= 1 day
      - "5h 23m"  when < 1 day
      - "23m"     when < 1 hour
      - "<1m"     when < 1 minute
      - "KICKOFF" when kickoff passed
    """
    ko = parse_iso(kickoff_iso)
    if ko is None:
        return ""
    ko_local = to_local(ko, tz)
    delta = ko_local - local_now(tz)
    secs = delta.total_seconds()
    if secs < 0:
        return "KICKOFF"
    if secs < 60:
        return "<1m"
    days = int(secs // 86400)
    hours = int((secs % 86400) // 3600)
    mins = int((secs % 3600) // 60)
    if days > 0:
        return f"{days}d {hours}h"
    if hours > 0:
        return f"{hours}h {mins}m"
    return f"{mins}m"
