# Fish Market Classification Model

## Problem Statement
The goal of this project is to build a classification model that predicts the species of fish in the market based on features such as weight, length, and height. This model helps identify the fish species from a dataset of various fish species commonly sold in the market.

## Model
- **Type:** Classification
- **Dataset:** Fish Market Dataset from Kaggle
- **Model:** DecisionTreeClassifier or RandomForestClassifier
- **Libraries Used:** Scikit-learn, Flask

## Steps
1. Preprocessing the data.
2. Train a classification model.
3. Save the model.
4. Deploy the model using Flask locally.

## How to Run the Project Locally
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Make sure you have the `fish_market_model.pkl` file in the same directory as the app.
4. Run the Flask app with the command:

   ```bash
   python app.py
