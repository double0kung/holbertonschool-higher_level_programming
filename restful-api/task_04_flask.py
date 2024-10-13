from flask import Flask, jsonify, request

app = Flask(__name__)
app.json.sort_keys = False

users = {}

@app.route("/")
def hello_world():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify([username for username in users])

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    try:
        return jsonify(users[username])
    except KeyError:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=['POST'])
def add_user():
    user = request.get_json()
    try:
        username = user['username']
        if username in users:
            return jsonify({"error": "Username already exists"}), 400
        users[username] = user
        return jsonify({"message": "User added", "user": user}), 200  # Changed to 200
    except KeyError:
        return jsonify({"error": "Username is required"}), 400

if __name__ == "__main__":
    app.run(debug=True)
