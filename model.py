from flask_restful import Resource, Api, reqparse
from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS
from keras.models import load_model
model = load_model('model_car')


app = Flask(__name__)
CORS(app)


@app.route("/predict", methods=["POST"])
def predict():
    result = 0
    if request.method == "POST":
        input_value = request.form['input_value']
        # Do some prediction
        data = [float(i)for i in str(input_value).split(",")]
        np_data = np.array(data).reshape(1, 10)
        y_predict = model.predict(np_data)
        result = str(y_predict.argmax(axis=1)[0])
    return jsonify(
        prediction=result,
    ), 201
