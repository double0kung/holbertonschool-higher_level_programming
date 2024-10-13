from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    if not user_data or 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400
    
    username = user_data['username']
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    
    # Ensure all required fields are present
    required_fields = ['username', 'name', 'age', 'city']
    if not all(field in user_data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Only store the required fields
    new_user = {field: user_data[field] for field in required_fields}
    users[username] = new_user
    
    return jsonify({
        "message": "User added",
        "user": new_user
    })

if __name__ == "__main__":
    app.run(debug=True)
