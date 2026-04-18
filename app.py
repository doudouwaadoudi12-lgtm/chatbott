from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# 🔹 Charger le fichier FAQ
def load_faq():
    with open("faq.json", "r", encoding="utf-8") as f:
        return json.load(f)

# 🔹 Page d’accueil
@app.route("/")
def home():
    return render_template("index.html")

# 🔹 Dashboard
@app.route("/dashboard")
def dashboard():
    faqs = load_faq()
    return render_template("dashboard.html", faqs=faqs)

# 🔹 API chatbot (réponse aux questions)
@app.route("/get_answer", methods=["POST"])
def get_answer():
    data = request.get_json()
    user_question = data.get("question", "").lower()

    faqs = load_faq()

    for item in faqs:
        if item["question"].lower() in user_question:
            return jsonify({"answer": item["answer"]})

    return jsonify({"answer": "Désolé, je n’ai pas compris votre question."})

# 🔹 Lancer l’application
if__name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)