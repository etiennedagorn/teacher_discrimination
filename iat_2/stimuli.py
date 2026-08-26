"""Load IAT stimuli from the app-level CSV file.

The CSV is the single source of stimuli for the light replication package. It
must contain the columns ``category`` and ``stimulus``. Category names must
match the labels configured in ``settings.py``.
"""

from __future__ import annotations

import csv
from pathlib import Path


STIMULI_CSV = Path(__file__).parent / "stimuli.csv"


def load_stimuli(path: Path = STIMULI_CSV) -> dict[str, list[str]]:
    """Return a category-to-stimuli mapping loaded from ``stimuli.csv``."""
    if not path.exists():
        raise FileNotFoundError(f"Missing IAT stimuli file: {path}")

    stimuli_by_category: dict[str, list[str]] = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required_columns = {"category", "stimulus"}
        missing_columns = required_columns - set(reader.fieldnames or [])
        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            raise ValueError(f"{path} is missing required column(s): {missing}")

        for row_number, row in enumerate(reader, start=2):
            if not any((value or "").strip() for value in row.values()):
                continue

            category = (row.get("category") or "").strip()
            stimulus = (row.get("stimulus") or "").strip()
            if not category or not stimulus:
                raise ValueError(f"{path}:{row_number} has an empty category or stimulus")

            stimuli_by_category.setdefault(category, []).append(stimulus)

    if not stimuli_by_category:
        raise ValueError(f"{path} does not contain any stimuli")

    return stimuli_by_category


DICT = load_stimuli()
