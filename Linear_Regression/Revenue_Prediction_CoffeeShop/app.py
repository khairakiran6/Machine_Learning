from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import logging
import numpy as np
from data_preprocessing  import preprocessing  # Import your preprocessing script

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
# Load the pre-trained Random Forest model (replace 'model.pkl' with your actual model file)
with open("LinearRegression.joblib", "rb") as f:
    model = joblib.load(f)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/classify', methods=['POST'])
def classify():
    data = None
    if 'csv_file' in request.files and request.files['csv_file'].filename != '':
        # Handle CSV upload
        csv_file = request.files['csv_file']
        data = pd.read_csv(csv_file)  ## data = pd.read_csv(csv_file,header=False)
    else:
        # Handle manual input        
        try:
            var1 = request.form['var1']
            var2 = request.form['var2']
            var3 = request.form['var3']
            data = pd.DataFrame([[var1,var2,var3]], columns=['Number_of_Customers_Per_Day','Average_Order_Value','Marketing_Spend_Per_Day'])
        except KeyError:
            return jsonify({"error": "Missing input. Ensure all variables are provided."}), 400

    # Preprocess the data using your preprocessing script
    try:
        processed_data = preprocessing(data)
    except Exception as e:
        return jsonify({"error": f"Preprocessing error: {str(e)}"}), 500

    # Perform classification
    try:
        predictions = model.predict(processed_data)
        print(f"Raw predictions: {predictions}")  # Debug raw predictions
        # Extract the first value from the array if it's a single prediction
        predicted_value = int(predictions[0] if isinstance(predictions, np.ndarray) else predictions)
        return jsonify({"predicted_revenue": predicted_value})
        
    except Exception as e:
        return jsonify({"error": f"Prediction error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
