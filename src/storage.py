from pathlib import Path

def save_users(df, path="data/users.csv"):
    """Write the DataFrame to CSV."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)