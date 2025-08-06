user_id = input("Enter user ID to delete: ")
url = f"http://127.0.0.1:5000/users/{user_id}"

response = requests.delete(url)

if response.status_code == 200:
    print(" User deleted successfully.")
else:
    print("User not found or already deleted.")
