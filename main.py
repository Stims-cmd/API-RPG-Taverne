from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # pour autoriser le fetch depuis le navigateur

# --- Données du joueur ---
player = {
    "name": "",
    "health": 150,
    "energy": 100,
    "level": 1
}

# --- Quêtes simples ---
quests = [
    {"id": 1, "title": "Nettoyer la cave", "description": "Des rats dans la cave", "reward": 50, "status": "available"},
    {"id": 2, "title": "Protéger la caravane", "description": "Escorter les marchands", "reward": 100, "status": "available"},
]

@app.route("/quests", methods=["GET"])
def get_quests():
    return jsonify(quests), 200

@app.route("/player/<name>", methods=["GET"])
def get_player(name):
    player["name"] = name
    return jsonify(player), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
