from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

users = []
products = [
    {
        "id": 1,
        "name": "Produto 1",
        "description": "Descrição do Produto 1",
        "price": 10.0,
        "imageFront": "https://localhost:5001/static/produto1.jpg",
        "imageBack": "https://localhost:5001/static/produto1_back.jpg",
        "inStock": True,
    }
]

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    users.append(data)
    return jsonify({"message": "Registrado com sucesso"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = next((u for u in users if u['username']==data['username']
                 and u['password']==data['password']), None)
    if user:
        return jsonify({"message": "Login ok"}), 200
    return jsonify({"error": "Credenciais inválidas"}), 401

@app.route('/api/products', methods=['GET'])
def list_products():
    #filtro por nome
    name = request.args.get('name')
    if name:
        filtered = [a for a in products if name.lower() in a['name'].lower()]
        return jsonify(filtered)
    return jsonify(products)

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    # gera novo id para o produto
    new_id = max((p['id'] for p in products), default=0) + 1
    product = {
        "id": new_id,
        "name": data.get['name'],
        "description": data.get['description'],
        "price": data.get['price'],
        "imageFront": data.get['imageFront'],
        "imageBack": data.get['imageBack'],
        "inStock": data.get['inStock', True],
    }
    products.append(product)
    return jsonify({"message": "Produto adicionado com sucesso"}), 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
