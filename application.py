import sys
import os

# Add project root path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask, request, render_template, redirect
import numpy as np
import pandas as pd

# Import your ML pipeline
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


# ✅ Create Flask app (IMPORTANT for AWS)
application = Flask(__name__)
app = application


# ✅ Home route (fixes blank/502 when opening domain)
@app.route('/')
def index():
    return redirect('/predictdata')


# ✅ Prediction route
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    try:
        if request.method == 'GET':
            return render_template('home.html')

        else:
            # ✅ Get input data from form (correct mapping)
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )

            # Convert to dataframe
            pred_df = data.get_data_as_data_frame()

            # Make prediction
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)

            # Send result to UI
            return render_template('home.html', results=round(results[0], 2))

    except Exception as e:
        # ✅ Prevents 502 crash
        return render_template('home.html', results=f"Error: {str(e)}")


# ✅ Run app locally and on AWS
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
