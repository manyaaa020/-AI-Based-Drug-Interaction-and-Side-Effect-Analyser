import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import os

# Load dataset
df = pd.read_csv("data/DDI_Severity_Labeled.csv")  # Use correct file name

# Preprocess
df.dropna(subset=['drug1_name', 'drug2_name', 'Severity Label'], inplace=True)
df['drug1_name'] = df['drug1_name'].str.lower().str.strip()
df['drug2_name'] = df['drug2_name'].str.lower().str.strip()
df['pair'] = df['drug1_name'] + " " + df['drug2_name']

# Encode target
label_encoder = LabelEncoder()
df['severity_encoded'] = label_encoder.fit_transform(df['Severity Label'])

# Vectorize
vectorizer = CountVectorizer(tokenizer=lambda x: x.split())
X = vectorizer.fit_transform(df['pair'])
y = df['severity_encoded']

# Split & Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, n_jobs=1, random_state=42)
model.fit(X_train, y_train)

# Save
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/severity_predictor.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model and components saved successfully in the 'models/' folder.")
joblib.dump(vectorizer, "models/vectorizer.pkl")
