from flask import Flask, jsonify, request, send_from_directory, render_template
from flask_cors import CORS
import os
import mysql.connector

app = Flask(__name__)
CORS(app)

# Route pour servir index.html
@app.route("/") 
def serve_index(): 
    return send_from_directory(os.getcwd(), "sitev2.html") 
#Route pour servir style.css
"""
@app.route("/style.css") 
def serve_css(): 
    return send_from_directory(os.getcwd(), "stylev2.css")
"""

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db"),
        user=os.getenv("MYSQL_USER", "user"),
        password=os.getenv("MYSQL_PASSWORD", "userpass"),
        database=os.getenv("MYSQL_DB", "quests_db")
    )


@app.route("/quests", methods=["GET"])
def get_quests():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM quests")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)


# CREATION DE QUETE 
@app.route("/quests", methods=["POST"])
def create_quest():
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
    quest_id = cur.lastrowid
    cur.close()
    conn.close()

    return jsonify({"id": quest_id, **data}), 201

# MODIFICATION QUETE
@app.route("/quests/<int:quest_id>", methods=["PUT"])
def update_quest(quest_id):
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

    return jsonify({"id": quest_id, **data})

# SUPPRESSION QUETE
@app.route("/quests/<int:quest_id>", methods=["DELETE"])
def delete_quest(quest_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM quests WHERE id = %s", (quest_id,))
    conn.commit()
    cur.close()
    conn.close()
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
