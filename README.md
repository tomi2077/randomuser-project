# Random User Project

A small Python pipeline that fetches sample user data from the [Random User Generator API](https://randomuser.me/), cleans and transforms it into a pandas DataFrame, runs basic analysis, and saves the results to CSV and SQLite. A lightweight FastAPI app also exposes the cleaned data and stats over HTTP, and a `Dockerfile` is included to run the whole thing in a container.

## What it does

1. **Fetch** — calls `https://randomuser.me/api/` and retrieves a batch of randomly generated user records.
2. **Transform** — flattens each raw user record into a simple dict (`first_name`, `last_name`, `gender`, `email`, `phone`, `city`, `country`), normalizes the `gender` field, drops duplicate rows, and fills missing values with `"Unknown"`.
3. **Analyse** — computes summary stats from the cleaned data: total user count, gender breakdown, top 5 countries, duplicate count, and null counts per column.
4. **Save** — writes the cleaned DataFrame to `data/users.csv` and to a `users` table in `data/users.db` (SQLite).

## Project structure

```
src/
  fetch.py           # calls the Random User API
  transform.py       # cleans raw records and builds the DataFrame
  analyse.py         # computes summary statistics
  storage.py         # writes the DataFrame to CSV and reads/writes it to SQLite
  api.py             # FastAPI app exposing /users and /stats endpoints
  main.py            # wires fetch -> transform -> analyse -> save together
  phase1_basics.py   # exploratory/learning script used while building the pipeline
tests/
  test_transform.py  # unit tests for the transform module
Dockerfile           # builds an image that runs main.py then serves api.py with uvicorn
pytest.ini
requirements.txt
```

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt` (key ones: `requests`, `pandas`, `matplotlib`, `pytest`, `fastapi`, `uvicorn`)

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

This fetches 20 users (with a fixed seed for reproducibility), cleans and transforms them, prints summary stats, and writes the result to `data/users.csv` and `data/users.db`.

### Running the API

The FastAPI app in `src/api.py` serves data out of `data/users.db`, so run `python src/main.py` at least once first to populate it:

```bash
python src/main.py
uvicorn api:app --reload --app-dir src
```

Endpoints:

- `GET /users` — reads the `users` table from SQLite; supports optional `country` and `gender` query filters (e.g. `/users?country=US&gender=female`).
- `GET /stats` — reads the `users` table and returns the same summary stats produced by `analyse_users`.

Note that the data only updates when `main.py` (or the Docker container, see below) is re-run — the API itself doesn't fetch live data.

### Running with Docker

The `Dockerfile` builds a self-contained image: it installs dependencies, then on container start runs `src/main.py` once (to fetch, clean, and save a batch of users into `data/users.db` inside the container) before launching the API.

```bash
docker build -t randomuser-project .
docker run -p 8000:8000 randomuser-project
```

The API is then available at `http://localhost:8000` (`/users`, `/stats`). Since the DB is populated once at container start, restart the container to refresh the data.

## Testing

Tests are configured via `pytest.ini` (which points `pythonpath` at `src/`). Run the suite with:

```bash
pytest
```

## Notes

- `data/` and `.env` are git-ignored — the CSV output is not committed.
- `src/phase1_basics.py` is a scratch/learning file documenting the step-by-step exploration of the API before it was refactored into the `fetch` / `transform` / `analyse` / `storage` modules used by `main.py`.
