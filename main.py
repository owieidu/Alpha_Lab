from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Rota principal da API
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "🚀 Alpha está online!"})

@app.route("/alpha", methods=["POST"])
def alpha_chat():
    data = request.json
    user_input = data.get("input", "")
    return jsonify({"response": f"[Free Mode] Resposta livre para: {user_input}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Railway usa variável de ambiente PORT
    app.run(host="0.0.0.0", port=port)
