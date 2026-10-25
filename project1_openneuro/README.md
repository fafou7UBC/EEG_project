# OpenNeuro EEG analysis

These notebooks use OpenNeuro dataset `ds003061`.

## Setup

From the repository root, install the project dependencies:

```powershell
python -m pip install -r project1_openneuro\requirements.txt
```

Open `project1_openneuro\notebooks\01_explore_data.ipynb` in VS Code and run
the cells in order. The shared loader downloads the dataset through the
official `openneuro-py` client into `project1_openneuro\data\ds003061` on the
first run. Later runs reuse the local files.

The other notebooks use the same local dataset and can be run independently
after the first download:

- `02_erp_p300.ipynb`
- `02b_erp_brain_visualization.ipynb`
- `03_classify_oddball.ipynb`

The dataset is ignored by Git; generated analysis results remain local.
