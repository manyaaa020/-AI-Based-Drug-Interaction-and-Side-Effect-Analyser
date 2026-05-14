# 💊 Drug-to-Drug Interaction Severity Predictor

> End-to-end ML pipeline for predicting drug interaction severity — built on a **self-constructed dataset** created through institutional collaboration and domain expert annotation.

**Patent Published:** Indian Patent Office Journal, Issue 1/2026 | App. No. 202521119855

---

## 🧩 The Problem — And Why the Dataset Didn't Exist

Drug-to-drug interactions (DDIs) are a leading cause of adverse clinical events. While interaction *existence* databases exist (e.g., DrugBank), **publicly available datasets labelled by interaction severity** (mild / moderate / severe) did not exist in a form suitable for ML classification.

Standard open datasets either:
- Lacked severity labels entirely
- Were too small for reliable model training
- Were restricted to proprietary clinical systems

---

## 📦 Dataset Construction — The Real Work

Building this dataset was the core research contribution of this project.

### Step 1 — Formal Data Requests
- Submitted a formal data access request to **DrugBank** for structured interaction records
- Supplemented with interaction data from additional pharmacological databases and published literature sources
- Combined and deduplicated entries across sources into a unified schema

### Step 2 — Medical Expert Collaboration
Recognising that automated sources alone were insufficient for severity annotation, we established a collaboration with:
- **SMCW (Shri Madhav College of Pharmacy / Medical students)** — contributed drug interaction knowledge from medical textbooks and clinical references
- **SUHRC Clinical Interns** — validated and annotated interaction severity levels based on clinical guidelines and pharmacovigilance standards

This human-in-the-loop annotation process ensured domain validity that purely automated pipelines cannot achieve.

### Step 3 — Dataset Assembly
- Final dataset: **500+ drug entries** with interaction pairs and severity labels
- Features: drug class, mechanism of action, interaction type, affected organ system, severity label
- Cleaned, deduplicated, and validated for class balance and annotation consistency

> 📢 **This dataset is being prepared for public release** — a contribution to the open pharmacological research community.

---

## 🔬 ML Pipeline

### Preprocessing
- NLP-based drug name standardisation (handling brand names, generics, abbreviations)
- Feature engineering: drug class encoding, interaction mechanism categories
- EDA: class distribution analysis, interaction frequency plots, missing value audit

### Models Trained & Evaluated

| Model | Validation Accuracy | Notes |
|---|---|---|
| Multinomial Naive Bayes | ~89% | Fast baseline, good for text features |
| Random Forest | ~94% | Best overall — selected for deployment |
| Logistic Regression | ~87% | Interpretable, good precision |

- 5-fold cross-validation for all models
- Confusion matrix, classification report, and ROC-AUC evaluated per class

### Key Features by Importance
1. Drug class combination
2. Mechanism of interaction
3. Affected physiological system
4. Dosage sensitivity flag

---

## 🖥️ Deployment

- **Streamlit Dashboard** — interactive risk visualisation, input any two drugs and get severity prediction with explanation
- **FastAPI endpoint** — `/predict` POST endpoint serving the trained Random Forest model
- **Full experiment documentation** — all preprocessing steps, model runs, and findings recorded

---

## 🛠️ Tech Stack

```
Python, Pandas, NumPy
Scikit-learn (Random Forest, Naive Bayes, Logistic Regression)
NLTK / spaCy (NLP preprocessing)
Matplotlib, Seaborn
Streamlit, FastAPI
Jupyter Notebook
```

---

## 📋 Project Structure

```
drug-interaction-predictor/
│
├── data/
│   ├── raw/                  ← Source data (DrugBank + supplementary)
│   ├── annotated/            ← Expert-annotated severity labels
│   └── final_dataset.csv     ← Cleaned, unified dataset
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   └── 03_Modelling.ipynb
│
├── app/
│   ├── streamlit_app.py
│   └── api.py (FastAPI)
│
├── models/
│   └── rf_model.pkl
│
└── README.md
```

---

## 🏆 Outcomes

- **Patent Published** — Indian Patent Office Journal (Issue 1/2026, App. No. 202521119855)
- Dataset annotation methodology validated by clinical interns
- Model pipeline achieving ~94% validation accuracy on held-out test set
- Dashboard deployed for interactive clinical exploration

---

## 👩‍💻 Authors

**Manya Sourabh Bhargava** — B.Tech AI/ML, Symbiosis Institute of Technology, Pune  
In collaboration with SMCW medical students and SUHRC clinical interns.

[GitHub](https://github.com/manyaaa020) | [LinkedIn](https://linkedin.com/in/manya-bhargava) | [Patent](https://ipindia.gov.in)
