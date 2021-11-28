from flask import Flask, jsonify, request
from classifier import get_prediction
import os, ssl 

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)
@app.route("/predict-digit",methods=["POST"])

def predict_data():
    image = request.files.get("alphabet")
    prediction = get_prediction(image)
    return jsonify({
        "prediction":prediction
    }),200

if __name__ == "__main__":
    app.run(debug = True)