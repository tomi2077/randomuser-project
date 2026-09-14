import pandas as pd

def clean_users(users):

    # cleaned_users = []
    
    # for user in users:
    #     new_dict = {
    #         'first_name': user['name']['first'],
    #         'last_name':  user['name']['last'],
    #         'gender': user['gender'],
    #         'email': user['email'],
    #         'phone': user['phone'],
    #         'city': user['location']['city'],
    #         'country': user['location']['country']
    #     }
    #     cleaned_users.append(new_dict)

    # return cleaned_users

    cleaned = []
    for user in users:
        new_dict = {
            'first_name': user.get('name', {}).get('first', 'Unknown'),
            'last_name': user.get('name', {}).get('last', 'Unknown'),
            'gender': user.get('gender', 'Unknown'),
            'email': user.get('email', 'Unknown'),
            'phone': user.get('phone', 'Unknown'),
            'city': user.get('location', {}).get('city', 'Unknown'),
            'country': user.get('location', {}).get('country', 'Unknown')
        }
        cleaned.append(new_dict)
    return cleaned


def create_dataframe(data):
    df = pd.DataFrame(data)
    df['gender'] = df['gender'].str.lower().str.strip()
    df = df.drop_duplicates()
    df['city'] = df['city'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')
    return df
