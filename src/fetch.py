import requests

def fetch_users(results=5, gender=None, nat=None, seed=None,
                base_url="https://randomuser.me/api/"):
    """Fetch users from the Random User API and return the list of user dicts."""
    params = {"results": results}
    if gender is not None:
        params["gender"] = gender
    if nat is not None:
        params["nat"] = nat
    if seed is not None:
        params["seed"] = seed

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error fetching users: {e}")
        return []

    return data["results"]

    