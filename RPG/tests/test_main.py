import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app
from unittest.mock import patch, MagicMock


# ----------------------------------------------------------
# ----------------- Test de la page html -------------------
# ----------------------------------------------------------
def test_serve_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200



# ----------------------------------------------------------
# ----------------- Test GET--------------------------------
# ----------------------------------------------------------

def test_get_quests():
    client = app.test_client()

    # Mock de la connexion MySQL
    fake_conn = MagicMock()
    fake_cursor = MagicMock()
    fake_cursor.fetchall.return_value = [
        {"id": 1, "title": "Test Quest"}
    ]
    fake_conn.cursor.return_value = fake_cursor
    with patch("main.get_db_connection", return_value=fake_conn):
        response = client.get("/quests")

    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert response.json[0]["title"] == "Test Quest"



# ----------------------------------------------------------
# ----------------- Test POST-------------------------------
# ----------------------------------------------------------
def test_create_quest():
    client = app.test_client()
    fake_conn = MagicMock()
    fake_cursor = MagicMock()
    fake_cursor.lastrowid = 42
    fake_conn.cursor.return_value = fake_cursor
    with patch("main.get_db_connection", return_value=fake_conn):
        response = client.post("/quests", json={
            "title": "Quest",
            "description": "Test",
            "reward": 100,
            "base_reward": 50,
            "status": "active",
            "modified": False
        })

    assert response.status_code == 201
    assert response.json["id"] == 42
    assert response.json["title"] == "Quest"



# ----------------------------------------------------------
# ----------------- Test PUT--------------------------------
# ----------------------------------------------------------
def test_update_quest():
    client = app.test_client()
    fake_conn = MagicMock()
    fake_cursor = MagicMock()
    fake_conn.cursor.return_value = fake_cursor
    with patch("main.get_db_connection", return_value=fake_conn):
        response = client.put("/quests/1", json={
            "title": "Updated",
            "description": "Updated desc",
            "reward": 200,
            "base_reward": 100,
            "status": "done",
            "modified": True
        })

    assert response.status_code == 200
    assert response.json["id"] == 1
    assert response.json["title"] == "Updated"



# ----------------------------------------------------------
# ----------------- Test DELETE-----------------------------
# ----------------------------------------------------------
def test_delete_quest():
    client = app.test_client()
    fake_conn = MagicMock()
    fake_cursor = MagicMock()
    fake_conn.cursor.return_value = fake_cursor
    with patch("main.get_db_connection", return_value=fake_conn):
        response = client.delete("/quests/1")
    assert response.status_code == 204
