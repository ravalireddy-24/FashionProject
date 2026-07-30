from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path
from typing import Iterable


def safe_filename(name: str) -> str:
    stem = re.sub(r"[^a-zA-Z0-9_-]+", "-", Path(name).stem).strip("-") or "upload"
    suffix = Path(name).suffix.lower()
    return f"{stem}-{hashlib.sha256(name.encode()).hexdigest()[:8]}{suffix}"


def parse_list(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [item.strip() for item in str(value).split(",") if item.strip()]


def json_dumps(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def unique(values: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))
