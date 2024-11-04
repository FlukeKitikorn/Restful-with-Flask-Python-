from flask import Flask, Request, jsonify

app = Flask(__name__)

user = [
    {"ID": 1,"name": "User 1","career": "Role 1"},
    {"ID": 2,"name": "User 2","career": "Role 2"},
    {"ID": 3,"name": "User 3","career": "Role 3"},
    {"ID": 4,"name": "User 4","career": "Role 4"},
    {"ID": 5,"name": "User 5","career": "Role 5"},
    {"ID": 6,"name": "User 6","career": "Role 6"},
    {"ID": 7,"name": "User 7","career": "Role 7"},
    {"ID": 8,"name": "User 8","career": "Role 8"},
    {"ID": 9,"name": "User 9","career": "Role 9"},
    {"ID": 10,"name": "User 10","career": "Role 10"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(user), 200

if __name__ == '__main__':
    app.run(debug=True)
