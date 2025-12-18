from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- Données en mémoire ---
quests = [
    {"id": 1, "title": "Nettoyer la cave", "description": "Des rats dans la cave",
     "reward": 50, "base_reward": 50, "status": "available", "modified": False},
    {"id": 2, "title": "Protéger la caravane", "description": "Escorter les marchands",
     "reward": 100, "base_reward": 100, "status": "available", "modified": False},
    {"id": 3, "title": "Trouver l'amulette perdue", "description": "Dans la forêt sombre",
     "reward": 150, "base_reward": 150, "status": "available", "modified": False}
]

# GET toutes les quêtes
@app.route("/quests", methods=["GET"])
def get_quests():
    return jsonify(quests), 200

# PATCH pour modifier titre, statut ou reward
@app.route("/quests/<int:quest_id>", methods=["PATCH"])
def update_quest(quest_id):
    data = request.get_json()
    for quest in quests:
        if quest["id"] == quest_id:
            # Modifier le titre
            if "title" in data:
                quest["title"] = data["title"]
            # Modifier le statut
            if "status" in data:
                quest["status"] = data["status"]
            # Modifier la récompense
            if "reward" in data:
                if quest["modified"]:
                    return jsonify({"error": "Cette quête ne peut plus être modifiée"}), 400
                new_reward = data["reward"]
                max_reward = 2 * quest["base_reward"]
                if new_reward > max_reward:
                    new_reward = max_reward
                quest["reward"] = new_reward
                quest["modified"] = True  # on marque la quête comme modifiée
            return jsonify(quest), 200
    return jsonify({"error": "Quête non trouvée"}), 404

# POST pour créer une nouvelle quête
@app.route("/quests", methods=["POST"])
def create_quest():
    data = request.get_json()
    new_id = max(q["id"] for q in quests) + 1 if quests else 1
    base_reward = data.get("reward", 0)
    new_quest = {
        "id": new_id,
        "title": data.get("title", f"Quête {new_id}"),
        "description": data.get("description", ""),
        "reward": base_reward,
        "base_reward": base_reward,
        "status": "available",
        "modified": False
    }
    quests.append(new_quest)
    return jsonify(new_quest), 201

# DELETE pour supprimer une quête
@app.route("/quests/<int:quest_id>", methods=["DELETE"])
def delete_quest(quest_id):
    global quests
    quests = [q for q in quests if q["id"] != quest_id]
    return jsonify({"message": "Quête supprimée"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
