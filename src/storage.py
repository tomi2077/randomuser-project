import sqlite3
import pandas as pd
from pathlib import Path


def save_users(df, path="data/users.csv"):
    """Write the DataFrame to CSV."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def save_to_db(df, db_path="data/users.db", table="users"):
    """Write the DataFrame to a SQLite table."""
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    df.to_sql(table, conn, if_exists="replace", index=False)
    conn.close()


def load_from_db(db_path="data/users.db", table="users"):
    """Read the users table from SQLite into a DataFrame."""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f"SELECT * FROM {table}", conn)
    conn.close()
    return df