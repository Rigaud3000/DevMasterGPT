from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
generator = pipeline("text-generation", model="tiiuae/falcon-rw-1b")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")
    result = generator(prompt, max_new_tokens=100)[0]['generated_text']
    return jsonify({"response": result})

@app.route("/")
def home():
    return {"message": "DevMasterGPT API is live!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
