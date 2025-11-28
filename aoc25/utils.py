from pathlib import Path
from typing import List


def read_to_list(path: Path) -> List[str]:
    """Read file and return a list of lines without trailing newlines."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def read_to_line(path: Path) -> str:
    """Read entire file and return as a single string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def read_to_string(path: Path) -> str:
    """Alias for `read_to_line` kept for compatibility."""
    return read_to_line(path)