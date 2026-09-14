# tests/test_transform.py
import sys
print(sys.path)
from transform import clean_users, create_dataframe


fake_users = [
    {"name": {"first": "Ada", "last": "Lovelace"}, "gender": "female",
     "email": "ada@example.com", "phone": "123",
     "location": {"city": "London", "country": "United Kingdom"}},
    {"name": {"first": "Alan", "last": "Turing"}, "gender": "male"}
]


def test_clean_users_returns_correct_count():
    result = clean_users(fake_users)
    assert len(result) == 2
def test_clean_users_produces_expected_keys():
    result = clean_users(fake_users)
    assert set(result[0].keys()) == {"first_name", "last_name", "gender",
                                     "email", "phone", "city", "country"}


def test_clean_users_fills_missing_fields():
    result = clean_users(fake_users)
    assert result[1]["email"] == "Unknown"
    assert result[1]["phone"] == "Unknown"
    assert result[1]["city"] == "Unknown"
    assert result[1]["country"] == "Unknown"


def test_create_dataframe_shape():
    df = create_dataframe(clean_users(fake_users))
    assert df.shape == (2, 7)