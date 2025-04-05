from flask import Flask, request, jsonify
import pickle

# Load the model pipeline (pickled model from Google Colab)
with open("sentiment_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Sentiment Analysis v1 PROD<h1>"

@app.route('/sentiment', methods=['POST'])
def predict_sentiment():
    input_data = request.json
    text = input_data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    prediction = model.predict([text])[0]

    return jsonify({"result": prediction})
    
    # return {"input_data": input_data, "message": "hello!"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)

    