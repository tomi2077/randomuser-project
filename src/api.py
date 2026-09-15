from fastapi import FastAPI
from fetch import fetch_users
from transform import clean_users, create_dataframe
from analyse import analyse_users

app = FastAPI()


@app.get("/users")
def get_users(country: str = None, gender: str = None):
    users = fetch_users(results=20)
    cleaned = clean_users(users)

    if country is not None:
        cleaned = [u for u in cleaned if u["country"] == country]
    if gender is not None:
        cleaned = [u for u in cleaned if u["gender"] == gender]

    return cleaned

@app.get("/stats")
def get_stats():
    users = fetch_users(results=20)
    cleaned = clean_users(users)
    df = create_dataframe(cleaned)
    return analyse_users(df)