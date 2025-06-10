import os
import joblib
from app.utils import clean_drug_name

# Paths
MODEL_PATH = os.path.join("models", "severity_predictor.pkl")
ENCODER_PATH = os.path.join("models", "label_encoder.pkl")
VECTORIZER_PATH = os.path.join("models", "vectorizer.pkl")

# Load everything
try:
    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(ENCODER_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
except Exception as e:
    model = None
    label_encoder = None
    vectorizer = None
    print("⚠️ Error loading model, encoder, or vectorizer:", e)

def predict_severity(drug1, drug2):
    if model is None or label_encoder is None or vectorizer is None:
        return "Model or vectorizer not available"

    drug1 = clean_drug_name(drug1)
    drug2 = clean_drug_name(drug2)

    X_input = vectorizer.transform([f"{drug1} {drug2}"])
    y_pred = model.predict(X_input)
    severity_label = label_encoder.inverse_transform(y_pred)[0]
    return severity_label
