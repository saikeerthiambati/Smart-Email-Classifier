from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend running successfully"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    email_text = data.get("email", "")

    # Dummy logic (temporary)
    if "urgent" in email_text.lower():
        category = "High Priority"
    else:
        category = "Normal Priority"

    return jsonify({
        "email": email_text,
        "prediction": category
    })

if __name__ == "__main__":
    app.run(debug=True)
