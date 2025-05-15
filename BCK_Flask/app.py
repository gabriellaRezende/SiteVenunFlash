from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

users = []
products = [
    {
        "id": 1,
        "name": "Checked Short Dress",
        "description": "Incrivel vestido para se usar em um dia enslo",
        "price": 24.99,
        "imageFront": "http://localhost:5001/static/DressFront1.jpg",
        "imageBack": "http://localhost:5001/static/DressBack1.jpg",
        "inStock": True,
    },
    {
        "id": 2,
        "name": "Slim Fit Chinos",
        "description": "Claça masculina elegante para o dia a dia",
        "price": 39.99,
        "imageFront": "http://localhost:5001/static/PantsFront.jpg",
        "imageBack": "http://localhost:5001/static/PantsBack.jpg",
        "inStock": True,
    },
    {
        "id": 3,
        "name": "Blue Round-Neck Tshirt",
        "description": "Tshirt de algodão com estampa",
        "price": 9.99,
        "imageFront": "http://localhost:5001/static/TshirtsFront.jpg",
        "imageBack": "http://localhost:5001/static/TshirtsBack.jpg",
        "inStock": False,
    },
    {
        "id": 4,
        "name": "Dark Brown Boots",
        "description": "Bota de couro marrom escuro",
        "price": 49,
        "imageFront": "http://localhost:5001/static/ShoesFront.jpg",
        "imageBack": "http://localhost:5001/static/ShoesBack.jpg",
        "inStock": False,
    },
    {
        "id": 5,
        "name": "Unisex Sunglasses",
        "description": "Óculos de sol unissex",
        "price": 11.99,
        "imageFront": "http://localhost:5001/static/SunglassesFront.jpg",
        "imageBack": "http://localhost:5001/static/SunglassesBack.jpg",
        "inStock": True,
    },
    {
        "id": 6,
        "name": "Blue Round-Neck Tshirt",
        "description": "Incrivel vestido para se usar em um dia enslo",
        "price": 9.99,
        "imageFront": "http://localhost:5001/static/DressFront2.jpg",
        "imageBack": "http://localhost:5001/static/DressBack2.jpg",
        "inStock": False,
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
        "name": data.get('name'),
        "description": data.get('description'),
        "price": data.get('price'),
        "imageFront": data.get('frontImage'),
        "imageBack": data.get('backImage'),
        "inStock": data.get('inStock', True),
    }
    products.append(product)
    return jsonify({"message": "Produto adicionado com sucesso"}), 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
