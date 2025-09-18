import requests

BASE_URL = "https://reqres.in/api"   

def get_user(user_id):
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.get(url)
    return response

def create_user(user_data):
    url = f"{BASE_URL}/users"
    response = requests.post(url, json=user_data)
    return response
