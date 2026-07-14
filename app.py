#flask,scikit-learn,pandas,pickle-mixin
import pandas as pd
from flask import Flask, render_template, request,jsonify
import pickle

import numpy as np
app = Flask(__name__)
data=pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open('DelhiHousePredictionModel.pkl', 'rb'))
@app.route('/')
def index():

    locations=sorted(data['location'].unique())
    type_of_buildings=data['type_of_building'].unique()
    return render_template('index.html', locations=locations, type_of_buildings=type_of_buildings)
@app.route('/predict',methods=['POST'])
def predict():
    location=request.form.get('location')
    type_of_building=request.form.get('type_of_building')
    Bedrooms=int(request.form.get('Bedrooms'))
    Bathrooms=int(request.form.get('Bathrooms'))
    area=float(request.form.get('area'))
    if area < 501 or area > 9500:
        return jsonify({
            "status": "error",
            "message": "Area must be between 501 and 9500 sqft"
        })

    if Bedrooms < 1 or Bedrooms > 10:
        return jsonify({
            "status": "error",
            "message": "Bedrooms must be between 1 and 10"
        })

    if Bathrooms < 1 or Bathrooms > 10:
        return jsonify({
            "status": "error",
            "message": "Bathrooms must be between 1 and 10"
        })
    print(location,type_of_building,Bedrooms,Bathrooms,area)
    input=pd.DataFrame([[location,type_of_building,Bedrooms,Bathrooms,area]],columns=['location','type_of_building','Bedrooms','Bathrooms','area'])


    prediction = pipe.predict(input)[0]

    return jsonify({
      "status": "success",
      "result": round(float(prediction), 0)
    })


if __name__ == "__main__":
    app.run(debug=True, port=5861)