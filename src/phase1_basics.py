# import the requests library
import requests

# store the API url in a variable: https://randomuser.me/api/
api_url = "https://randomuser.me/api/"
params = {"results": 5}

# send a GET request to that url, store the result in `response`
response = requests.get(api_url, params=params)

# print the type of `response`  -- what is this object?
print(type(response))

# print the status code
print(response.status_code)

# print the type of the status code
print(type(response.status_code))


# print the first 300 characters of response.text
response_text = response.text
print(response_text[0:301])

# print the type of response.text
print(type(response_text))

# convert the response body to a Python object using .json()
# store it in `data`

data = response.json()

# print the type of `data`
# print(type(data))                    # dict
# print(data.keys())                   # what are the top-level keys?

# print(type(data["results"]))         # ?
# print(len(data["results"]))          # how many users?

# user = data["results"][0]
# print(type(user)) 
# print('======================')                   # ?
# print(user.keys())                   # what does one user contain?
# print('======================')   
# print(type(user["name"]))            # ?
# print(user["name"])
# print(user["name"]["first"])

# print('=====================PHASE-2==========================') 
# print(type(user["location"]))
# print(user["location"].keys())

# print(type(user["location"]["coordinates"]))
# print(user["location"]["coordinates"]["latitude"])

# print(type(user["picture"]))
# print(user["picture"].keys())

print('=====================PHASE-3==========================') 
users = data['results']
user = users[0]
for key, value in user.items():
    print(key, "->", type(value).__name__)

print('=====================PHASE-3 results==========================') 

# for user in users:
#     print(f"First Name: {user['name']['first']}, "
#           f"Last Name: {user['name']['last']}, "
#           f"Email: {user['email']}, "
#           f"Gender: {user['gender']}, "
#           f"Phone: {user['phone']}, "
#           f"City: {user['location']['city']}, "
#           f"Country: {user['location']['country']}")

print('=====================PHASE-3b results==========================') 

clean_users = []
for user in users:
  new_dict = {"first_name": user['name']['first'],
              "last_name": user['name']['last'],
              "email": user['email'],
              "gender": user['gender'],
              "phone": user['phone'],
              "city": user['location']['city'],
              "country": user['location']['country']}
  clean_users.append(new_dict)

print(len(clean_users))
print(clean_users[0])
print(type(clean_users))
print(type(clean_users[0]))

print('=====================PHASE-4 API==========================')
def fetch_users(results=5, gender=None, nat=None, seed=None,base_url="https://randomuser.me/api/"):
  params = {"results": results}
  if gender is not None:
    params['gender'] = gender
  if nat is not None:
    params['nat'] = nat
  if seed is not None:
    params['seed'] = seed
  # send the request
  response = requests.get(base_url, params=params)
  data = response.json()
  return data["results"]


fetch_users(results = 5, gender = 'female', nat = 'DK', seed = 'Tominiyi' )

