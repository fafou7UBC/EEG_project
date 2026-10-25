"""Shared OpenNeuro dataset access for the project notebooks."""

from __future__ import annotations

from pathlib import Path

DATASET_ID = "ds003061"
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_ROOT = PROJECT_ROOT / "data" / DATASET_ID


def ensure_dataset() -> Path:
    """Download the configured OpenNeuro dataset when it is not present."""
    if any(DATA_ROOT.glob("sub-*/eeg/*_eeg.set")):
        return DATA_ROOT

    try:
        import openneuro
    except ImportError as error:
        raise ImportError(
            "The OpenNeuro client is required. Install project dependencies "
            "with `python -m pip install -r requirements.txt`."
        ) from error

    DATA_ROOT.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading OpenNeuro {DATASET_ID} to {DATA_ROOT}...")
    openneuro.download(
        dataset=DATASET_ID,
        target_dir=str(DATA_ROOT),
    )
    return DATA_ROOT
