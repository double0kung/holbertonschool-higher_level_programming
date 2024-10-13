#!/usr/bin/python3
"""
0. Read file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:
"""
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
        return users[username]
    except KeyError:
        return jsonify({"error": "User not found"}), 404


@app.post("/add_user")
def add_user():
    user = request.get_json()
    try:
        users[user['username']] = user
        return jsonify({"message": "User added", "user": user}), 201
    except KeyError:
        return jsonify({"error": "Username is required"}), 400


if __name__ == "__main__":
    app.run()
