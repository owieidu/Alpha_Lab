from flask import Flask, request, jsonify
import os
from transformers import pipeline

app = Flask(__name__)

# Carregar modelo de linguagem pequeno
generator = pipeline("text-generation", model="distilgpt2")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "🚀 Alpha está online com IA HuggingFace!"})

@app.route("/alpha", methods=["POST"])
def alpha_chat():
    data = request.json
    user_input = data.get("input", "")

    # Gerar resposta com HuggingFace
    response = generator(user_input, max_length=80, num_return_sequences=1)
    answer = response[0]['generated_text']

    return jsonify({"response": answer})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
