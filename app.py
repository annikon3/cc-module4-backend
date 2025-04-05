from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os

# Sources: https://docs.python.org/3/library/pickle.html#module-pickle

load_dotenv()
API_TOKEN = os.environ.get("API_TOKEN")

app = Flask(__name__)
CORS(app)

# Load the model pipeline (pickled model from Google Colab)
with open("sentiment_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "<h1>Sentiment Analysis v1.2 PROD<h1>"


@app.route('/sentiment', methods=['POST'])
def predict_sentiment():
    # Token Auth 
    auth_header = request.headers.get("Authorization", "")
    if not auth_header or auth_header != f"Bearer {API_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401

    # Handle Input Data
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Sentiment Analysis Prediction
    prediction = model.predict([text])[0]
    return jsonify({"result": prediction})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)

    