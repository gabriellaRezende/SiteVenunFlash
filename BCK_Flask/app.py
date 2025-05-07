from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []
articles = [
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

@app.route('/api/articles', methods=['GET'])
def list_articles():
    name = request.args.get('name')
    if name:
        filtered = [a for a in articles if name.lower() in a['name'].lower()]
        return jsonify(filtered)
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)
