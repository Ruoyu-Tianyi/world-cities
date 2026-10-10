# California Housing Data App Lab

Author: Tianyi Zhou

This folder is the second app in the world-cities repository.
It uses the repository's Python 3.14 environment and locked dependencies.

## Run

From the repository root:

```powershell
uv run streamlit run housing-lab/app-housing.py
```

## Lab requirements

- Title includes the author's name.
- Minimum house value: 0 through 500001, default 200000 (US dollars).
- All five ocean proximity categories selected initially.
- Income radio: Low <= 2.5; Medium > 2.5 and < 4.5; High >= 4.5.
- Income is measured in tens of thousands of US dollars. Low is selected initially.
- Map of matching districts, followed by a histogram with exactly 30 bins.
- Empty selections show a helpful message and an empty histogram without crashing.

## Data

`housing.csv` is the standard 20,640-row California housing dataset used in
Hands-On Machine Learning. Each row represents a 1990 district.
Source: https://github.com/ageron/handson-ml2/blob/master/datasets/housing/housing.csv

The user-supplied course housing.csv was verified byte-for-byte identical to this
file (SHA-256: 8a3727f4cf54ac1a327f69b1d5b4db54c5834ea81c6e4efc0d163300022a685e).
It has all required columns, five location types, and house value range 14999 to
500001. Missing values in the unused total_bedrooms column are left unchanged;
no districts are dropped.

## Streamlit Community Cloud

Create a second app; keep the existing World Cities app.

- Repository: Ruoyu-Tianyi/world-cities
- Branch: main
- Main file path: housing-lab/app-housing.py
- Advanced settings / Python: 3.14

Cloud installs dependencies from the root uv.lock and pyproject.toml.
