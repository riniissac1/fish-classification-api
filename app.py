from flask import Flask, request, render_template
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the trained model
model = joblib.load("fish_market_model.pkl")

# Manually create and fit the LabelEncoder directly with the species labels
encoder = LabelEncoder()
encoder.fit(["Bream", "Roach", "Whitefish", "Parkki", "Perch", "Pike", "Smelt"])  # Replace with the actual species names

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get data from form (assuming the form sends all 6 features in the correct order)
        features = [float(x) for x in request.form.values()]
        features = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)

        # Decode prediction if it's label-encoded
        decoded_species = encoder.inverse_transform(prediction)

        return render_template("index.html", prediction_text=f"Predicted Fish Species: {decoded_species[0]}")
    except Exception as e:
        return render_template("index.html", prediction_text="Error: " + str(e))

if __name__ == "__main__":
    app.run(debug=True)
