user_id = input("Enter user ID to update: ")
new_name = input("Enter new name: ")
new_email = input("Enter new email: ")

url = f"http://127.0.0.1:5000/users/{user_id}"
data = {
    "name": new_name,
    "email": new_email
}

response = requests.put(url, json=data)

if response.status_code == 200:
    print(" User updated successfully:")
    print(response.json())
else:
    print(" User not found or update failed.")
