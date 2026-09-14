# Random User Project

A small Python pipeline that fetches sample user data from the [Random User Generator API](https://randomuser.me/), cleans and transforms it into a pandas DataFrame, runs basic analysis, and saves the results to CSV.

## What it does

1. **Fetch** — calls `https://randomuser.me/api/` and retrieves a batch of randomly generated user records.
2. **Transform** — flattens each raw user record into a simple dict (`first_name`, `last_name`, `gender`, `email`, `phone`, `city`, `country`), normalizes the `gender` field, drops duplicate rows, and fills missing values with `"Unknown"`.
3. **Analyse** — computes summary stats from the cleaned data: total user count, gender breakdown, top 5 countries, duplicate count, and null counts per column.
4. **Save** — writes the cleaned DataFrame to `data/users.csv`.

## Project structure

```
src/
  fetch.py           # calls the Random User API
  transform.py       # cleans raw records and builds the DataFrame
  analyse.py         # computes summary statistics
  storage.py         # writes the DataFrame to CSV
  main.py            # wires fetch -> transform -> analyse -> save together
  phase1_basics.py   # exploratory/learning script used while building the pipeline
tests/
  test_transform.py  # unit tests for the transform module
pytest.ini
requirements.txt
```

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt` (key ones: `requests`, `pandas`, `matplotlib`, `pytest`)

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate      # on Windows
pip install -r requirements.txt
```

## Usage

Run the pipeline end to end:

```bash
python src/main.py
```

This fetches 20 users (with a fixed seed for reproducibility), cleans and transforms them, prints summary stats, and writes the result to `data/users.csv`.

## Testing

Tests are configured via `pytest.ini` (which points `pythonpath` at `src/`). Run the suite with:

```bash
pytest
```

## Notes

- `data/` and `.env` are git-ignored — the CSV output is not committed.
- `src/phase1_basics.py` is a scratch/learning file documenting the step-by-step exploration of the API before it was refactored into the `fetch` / `transform` / `analyse` / `storage` modules used by `main.py`.
