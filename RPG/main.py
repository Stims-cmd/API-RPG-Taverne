from flask import Flask, jsonify, request, send_from_directory, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Route pour servir index.html
@app.route("/") 
def serve_index(): 
    return send_from_directory(os.getcwd(), "index.html") 
#Route pour servir style.css
@app.route("/style.css") 
def serve_css(): 
    return send_from_directory(os.getcwd(), "style.css")

# --- Données en mémoire ---
quests = [
    {"id": 1, "title": "Protéger la caravane",
     "description": "Le cousin Momo dit qu’il a vu des gadjé rôder près du camp. Achète un douze, sors le Dobermann, et montre-leur que la caravane, c’est sacré, frère.",
     "reward": 100, "base_reward": 100, "status": "available", "modified": False},

    {"id": 2, "title": "Le casse de la ferraille bénite",
     "description": "Un gadjo a volé ton radiateur en cuivre béni par le padrino. Infiltre sa casse, récupère ta ferraille... et pourquoi pas sa roumnia aussi, pour l’honneur.",
     "reward": 150, "base_reward": 150, "status": "available", "modified": False},

    {"id": 3, "title": "Le champion du barbecue",
     "description": "Le feu c’est la vie, frère. Fais cuire un sanglier entier avant la tombée du jour avec un tas de pneus et trois bidons d’essence. Si ça fume pas jusqu’à la nationale, c’est raté.",
     "reward": 120, "base_reward": 120, "status": "available", "modified": False},

    {"id": 4, "title": "Du gasoil ou du sang",
     "description": "Ta bagnole a soif, et les stations sont fermées. Siphonne trois véhicules avant le lever du jour. Fais vite, les keufs aiment pas les bricoleurs de nuit.",
     "reward": 130, "base_reward": 130, "status": "available", "modified": False},

    {"id": 5, "title": "Rêve de Kévin",
     "description": "Ta 306 mérite le respect du clan. Monte-lui des pièces de tuning, des bandes LED Temu, un aileron de Boeing, et roule vers la gloire. Si ça clignote plus qu’un mariage à Carpentas, t’as gagné.",
     "reward": 200, "base_reward": 200, "status": "available", "modified": False},

    {"id": 6, "title": "Le trésor du lithium",
     "description": "On raconte que sous un vieux rond-point, y’a un stock de batteries lithium oubliées. Déterre le trésor avec la tribu et va le revendre au marché noir. Le cuivre, c’est fini, le futur, c’est les piles !",
     "reward": 250, "base_reward": 250, "status": "available", "modified": False},

    {"id": 7, "title": "Le camion du destin",
     "description": "Monte dans ton vieux camion, fais le tour de la ville et remplis ta benne de ferraille. Plus t’en trouves, plus t’es respecté au camp. N’oublie pas : tout ce qui brille, c’est métal.",
     "reward": 180, "base_reward": 180, "status": "available", "modified": False},

    {"id": 8, "title": "Mariachh et Niversaaaaiiire !",
     "description": "Ta femme veut lancer Mariachhhh & Niversaaaaaire, un service d’événements un peu spécial. Il deviendra connu sur les réseaux.",
     "reward": 160, "base_reward": 160, "status": "available", "modified": False},

    {"id": 9, "title": "La SNCF est en retard (encore)",
     "description": "Y’a des kilomètres de câbles qui dorment sur les rails, mon frère. Va leur alléger un peu la voie et ramène tout au camp. Fais vite avant que les flics comprennent pourquoi plus rien roule.",
     "reward": 220, "base_reward": 220, "status": "available", "modified": False},

    {"id": 10, "title": "Le calibre de Kendji",
     "description": "Apprends à manier ton fusil et ta meuf sans te tirer dessus — y’en a qu’ont essayé, y chantent moins bien maintenant.",
     "reward": 300, "base_reward": 300, "status": "available", "modified": False}
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
