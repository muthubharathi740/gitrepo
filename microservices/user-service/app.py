from flask import Flask, request, jsonify 
 
app = Flask(__name__) 
 
@app.route('/users/login', methods=['POST']) 
def login_user(): 
    data = request.json 
    return jsonify({"message": "User authenticated successfully", "data": 
data}), 200 
 
@app.route('/users/<int:id>', methods=['GET']) 
def get_user(id): 
    return jsonify({"id": id, "name": "John Doe"}), 200 
 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)
