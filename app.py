from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = np.array2string(model.predict(data['input_data']))
    return jsonify(prediction)

if __name__ == '__main__':
    model = joblib.load('model.joblib')
    app.run(debug=True)
