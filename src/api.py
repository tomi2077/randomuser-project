from fastapi import FastAPI
from storage import load_from_db
from analyse import analyse_users

app = FastAPI()


@app.get("/users")
def get_users(country: str = None, gender: str = None):
    df = load_from_db()
    cleaned = df.to_dict(orient="records")

    if country is not None:
        cleaned = [u for u in cleaned if u["country"] == country]
    if gender is not None:
        cleaned = [u for u in cleaned if u["gender"] == gender]

    return cleaned


@app.get("/stats")
def get_stats():
    df = load_from_db()
    return analyse_users(df)