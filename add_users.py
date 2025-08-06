name = input("Enter new user's name: ")
email = input("Enter new user's email: ")

url = "http://127.0.0.1:5000/users"
data = {
    "name": name,
    "email": email
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print(" User created successfully:")
    print(response.json())
else:
    print(" Failed to create user.")
