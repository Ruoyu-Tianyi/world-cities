# World Cities

A Streamlit app for exploring cities with populations over one million.
Population values are in millions. Filter by minimum population, capital type,
and country; view matching cities on a map, in a table, and in a country chart.
Country names ignore case and surrounding spaces. Enter ALL and click Apply to reset.
Country totals include only the cities matching the current filters, not the entire country.

## Run locally

From this folder, with uv installed:

```powershell
uv sync
uv run streamlit run app-cities.py
```

Python 3.14 is required. `app.py` is a compatibility entry point.

## Deploy

Publish this folder as a public GitHub repository. Include `app-cities.py`,
`app.py`, `worldcities.csv`, `pyproject.toml`, `uv.lock`, `.python-version`,
`.gitignore`, and this README. Do not publish `.venv`.

At https://share.streamlit.io/ create an app from the repository:

- Branch: `main`
- Main file path: `app-cities.py`
- Advanced settings / Python version: `3.14`

Deploy and wait for the build to succeed. Later pushes redeploy automatically.
