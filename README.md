💊 AI-Based Drug Interaction and Side Effect Analyser

This project is a deployable web-based application designed to enhance medication safety using Artificial Intelligence. It allows users—both healthcare professionals and general individuals—to check drug-drug interactions, understand potential side effects, and receive real-time severity predictions for various drug combinations.

🧠 Key Features :

Drug Interaction Checker: Enter one or more drug names to detect known interactions with severity ratings (Mild, Moderate, Severe).
Conversational Chatbot: Powered by Google’s Gemini API, users can ask natural language questions like “Can I take Ibuprofen with Metformin?” and receive informative, human-like responses.
Severity Prediction Engine: Uses a Multinomial Naive Bayes classifier trained on labeled datasets to predict severity of unseen drug combinations.
User-Friendly Interface: Built using Streamlit for intuitive use and fast deployment.

🔧 Technology Stack :

Frontend/UI: Streamlit
Backend/ML: Python, scikit-learn, pandas, NumPy
Chatbot: Google Generative AI (Gemini API), Regex, YAKE for keyword extraction
Datasets: db_drug_interactions.csv, DDI_Severity_Labeled.csv

📈 Impact :

Reduces dependency on traditional, expensive clinical trials for drug interaction detection.
Provides accessible, fast, and accurate DDI analysis for better prescription decisions.
Promotes awareness and safe medication practices through AI-driven insights.

