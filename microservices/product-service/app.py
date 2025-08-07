from flask import Flask, jsonify, request 
app = Flask(__name__) 
products = [ 
    {"id": 1, "name": "Laptop", "price": 1000, "stock": 10}, 
    {"id": 2, "name": "Mouse", "price": 20, "stock": 200}, 
    {"id": 3, "name": "Keyboard", "price": 50, "stock": 150}, 
] 
@app.route('/products', methods=['GET']) 
def get_products(): 
    return jsonify(products) 
@app.route('/products/<int:product_id>', methods=['GET']) 
def get_product(product_id): 
    product = next((p for p in products if p["id"] == product_id), None) 
    if product: 
        return jsonify(product) 
    return jsonify({"error": "Product not found"}), 404 
 
if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5001)
