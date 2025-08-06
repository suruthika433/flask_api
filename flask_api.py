#FLASK CODE TO MANAGE USER DATA

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user database
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return {"message": "User not found"}, 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = data
    return {"message": "User created", "user": users[new_id]}, 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id].update(data)
        return {"message": "User updated", "user": users[user_id]}
    return {"message": "User not found"}, 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return {"message": "User deleted"}
    return {"message": "User not found"}, 404

if __name__ == '__main__':
    app.run(port=5000, use_reloader=False)
with open("flask_api.py", "w") as f:
    f.write(code)
    
!python flask_api.py

