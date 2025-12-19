from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import mysql.connector

# ------------------------------------------------------------
# Initialisation de l'application Flask
# ------------------------------------------------------------
app = Flask(__name__)
CORS(app)  # Autorise les requêtes venant d'autres origines (front, JS, etc.)


# ------------------------------------------------------------
# ROUTES POUR SERVIR LES FICHIERS HTML / CSS
# ------------------------------------------------------------

@app.route("/")
def serve_index():
    """
    Route principale : renvoie la page HTML.
    Le fichier 'sitev2.html' doit être dans le même dossier que ce script.
    """
    return send_from_directory(".", "sitev2.html")


@app.route("/style.css")
def serve_css():
    """
    Route pour servir le fichier CSS.
    Le fichier 'stylev2.css' doit être dans le même dossier que ce script.
    """
    return send_from_directory(".", "stylev2.css")


# ------------------------------------------------------------
# FONCTION : Connexion à la base MySQL
# ------------------------------------------------------------

def get_db_connection():
    """
    Crée et renvoie une connexion MySQL.
    Les paramètres viennent des variables d'environnement (Docker-friendly).
    """
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db"),
        user=os.getenv("MYSQL_USER", "user"),
        password=os.getenv("MYSQL_PASSWORD", "userpass"),
        database=os.getenv("MYSQL_DB", "quests_db")
    )


# ------------------------------------------------------------
# ROUTE : Récupérer toutes les quêtes
# ------------------------------------------------------------

@app.route("/quests", methods=["GET"])
def get_quests():
    """
    Récupère toutes les quêtes dans la base MySQL.
    Renvoie une liste de dictionnaires JSON.
    """
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM quests")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(rows), 200


# ------------------------------------------------------------
# ROUTE : Créer une nouvelle quête
# ------------------------------------------------------------

@app.route("/quests", methods=["POST"])
def create_quest():
    """
    Crée une nouvelle quête dans la base MySQL.
    Les champs doivent être fournis dans le JSON envoyé par le client.
    """
    data = request.json

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO quests (title, description, reward, base_reward, status, modified)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            data["title"],
            data["description"],
            data["reward"],
            data["base_reward"],
            data["status"],
            data.get("modified", False),
        ),
    )

    conn.commit()
    quest_id = cur.lastrowid  # ID auto-incrémenté de la nouvelle quête

    cur.close()
    conn.close()

    return jsonify({"id": quest_id, **data}), 201


# ------------------------------------------------------------
# ROUTE : Modifier une quête existante
# ------------------------------------------------------------

@app.route("/quests/<int:quest_id>", methods=["PUT"])
def update_quest(quest_id):
    """
    Met à jour une quête existante dans MySQL.
    Tous les champs doivent être fournis dans le JSON.
    """
    data = request.json

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE quests
        SET title = %s,
            description = %s,
            reward = %s,
            base_reward = %s,
            status = %s,
            modified = %s
        WHERE id = %s
        """,
        (
            data["title"],
            data["description"],
            data["reward"],
            data["base_reward"],
            data["status"],
            data.get("modified", False),
            quest_id,
        ),
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"id": quest_id, **data}), 200


# ------------------------------------------------------------
# ROUTE : Supprimer une quête
# ------------------------------------------------------------

@app.route("/quests/<int:quest_id>", methods=["DELETE"])
def delete_quest(quest_id):
    """
    Supprime une quête de la base MySQL selon son ID.
    """
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM quests WHERE id = %s", (quest_id,))
    conn.commit()

    cur.close()
    conn.close()

    return "", 204  # 204 = succès sans contenu


# ------------------------------------------------------------
# LANCEMENT DU SERVEUR
# ------------------------------------------------------------

if __name__ == "__main__":
    """
    Lancement du serveur Flask.
    Accessible sur : http://localhost:5000
    """
    app.run(host="0.0.0.0", port=5000, debug=True)
