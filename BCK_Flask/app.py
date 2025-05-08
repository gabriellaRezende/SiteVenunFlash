from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

users = []
products = [
    {"id": 1, "name": "Artigo A", "description": "Descrição A"},
    {"id": 2, "name": "Artigo B", "description": "Descrição B"},
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
    name = request.args.get('name')
    if name:
        filtered = [a for a in products if name.lower() in a['name'].lower()]
        return jsonify(filtered)
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
