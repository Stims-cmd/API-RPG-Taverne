from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def interaction():
        nom = request.args.get("nom", "Guardian")
        return jsonify({"message": f"Bonjour {nom}"}), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
