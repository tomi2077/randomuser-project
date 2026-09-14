from fetch import fetch_users
from transform import clean_users, create_dataframe
from analyse import analyse_users
from storage import save_users

users = fetch_users(results=20, seed="test")


cleaned = clean_users(users)

df = create_dataframe(cleaned)
stats = analyse_users(df)

print(len(cleaned))
print(cleaned[0])

print(df.shape)
print(df["gender"].value_counts())
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(len(cleaned) == 20)
print(list(cleaned[0].keys()))

print(df.shape == (20, 7))
print(df["gender"].value_counts())

print("XXXXXXXXXXXXXXXSTATSXXXXXXXXXXXXXXXXXXXXX")
print(stats)
save_users(df)