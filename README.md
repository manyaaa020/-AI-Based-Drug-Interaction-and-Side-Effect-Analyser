# AI-Based Drug Interaction & Side Effect Analyser

> End-to-end ML pipeline for predicting drug-drug interaction (DDI) severity — built on a **self-constructed, expert-annotated dataset** created through institutional collaboration with medical students and clinical interns.

**Patent Published:** Indian Patent Office Journal, Issue 1/2026 | App. No. 202521119855

---

## The Problem — And Why the Dataset Had to Be Built From Scratch

Drug-to-drug interactions (DDIs) are a leading cause of adverse clinical events globally. While databases documenting interaction *existence* are available (e.g., DrugBank), **no publicly available dataset existed with structured severity labels** (mild / moderate / severe) suitable for ML classification at the time of this project.

Standard open resources either:
- Lacked severity labels entirely
- Were too small for reliable model training
- Were locked behind proprietary clinical systems

---

## Dataset Construction — The Core Research Contribution

Building this dataset was the primary research challenge of the project. Two datasets are included in this repository:

| File | Description |
|---|---|
| `db_drug_interactions.csv` | Raw interaction records sourced from DrugBank and supplementary pharmacological databases |
| `DDI_Severity_Labeled.csv` | Final cleaned, annotated dataset with severity labels — ready for ML |

### How It Was Built

**Step 1 — Formal Data Requests**
- Submitted a formal access request to **DrugBank** for structured drug interaction records
- Supplemented with data from additional pharmacological literature and open drug databases
- Merged and deduplicated entries across sources into a unified schema

**Step 2 — Medical Expert Annotation (Human-in-the-Loop)**

Automated sources alone were insufficient for severity labelling. We collaborated with:
- **SMCW medical students** — contributed interaction knowledge from medical textbooks and clinical references
- **SUHRC clinical interns** — validated and annotated severity levels (mild / moderate / severe) based on pharmacovigilance standards and clinical guidelines

This human-in-the-loop process ensured domain validity that purely automated pipelines cannot replicate.

**Step 3 — Cleaning & Validation**
- Removed duplicates and inconsistently labelled entries
- Balanced class representation across severity levels
- Final dataset: **500+ drug entries** with interaction pairs and severity labels

> This dataset is being prepared for **public release** as a contribution to the open pharmacological research community.

---

## Project Structure

```
AI-Based-Drug-Interaction-and-Side-Effect-Analyser/
│
├── DDI_Severity_Labeled.csv      ← Final annotated dataset (custom-built)
├── db_drug_interactions.csv      ← Raw DrugBank source data
│
├── ml_predictor.py               ← ML training & evaluation pipeline
├── interaction_checker.py        ← Core interaction lookup & severity logic
├── chatbot_engine.py             ← Conversational query interface
├── main_app.py                   ← Streamlit dashboard (entry point)
├── utils.py                      ← Shared helper functions
├── _init_.py
│
├── requirements.txt
└── README.md
```

---

## ML Pipeline (`ml_predictor.py`)

### Preprocessing
- NLP-based drug name standardisation — handles brand names, generics, abbreviations
- Feature encoding: drug class, interaction mechanism, affected organ system
- EDA: class distribution, interaction frequency, missing value audit

### Models Trained & Evaluated

| Model | Validation Accuracy | Notes |
|---|---|---|
| Multinomial Naive Bayes | ~89% | Fast baseline, strong on text features |
| Random Forest | ~94% | Best overall — selected for deployment |
| Logistic Regression | ~87% | Interpretable, strong precision |

- 5-fold stratified cross-validation on all models
- Confusion matrix, classification report, and ROC-AUC per class
- Feature importance analysis — drug class combination and interaction mechanism are top predictors

---

## Application (`main_app.py`)

Built with **Streamlit** — run locally with one command:

```bash
streamlit run main_app.py
```

**Features:**
- Input any two drug names → get predicted severity (mild / moderate / severe)
- Confidence score per prediction
- Interaction mechanism explanation
- Chatbot interface via `chatbot_engine.py` for natural language queries

---

## Setup

```bash
# Clone the repo
git clone https://github.com/manyaaa020/-AI-Based-Drug-Interaction-and-Side-Effect-Analyser
cd -AI-Based-Drug-Interaction-and-Side-Effect-Analyser

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run main_app.py
```

---

## requirements.txt

```
pandas==2.1.0
numpy==1.25.0
scikit-learn==1.3.0
nltk==3.8.1
streamlit==1.28.0
matplotlib==3.7.2
seaborn==0.12.2
joblib==1.3.2
```

---

## Key Results

| Metric | Value |
|---|---|
| Best Model | Random Forest |
| Validation Accuracy | ~94% |
| Patent Status | Published — IPO Journal Issue 1/2026 |
| Dataset Size | 500+ drug interaction pairs |
| Severity Classes | Mild / Moderate / Severe |

---

## Outcomes

- **Patent Published** — Indian Patent Office Journal (Issue 1/2026, App. No. 202521119855)
- Custom dataset annotated by medical domain experts
- Interactive Streamlit app for clinical exploration
- All experiments, methodology, and dataset construction fully documented

---

## Authors

**Manya Sourabh Bhargava, Aakash Sharma ,Khushi Kashyap**

In collaboration with **SMCW medical students** and **SUHRC clinical interns** for dataset annotation and domain validation.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Manya_Bhargava-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/manya-bhargava)
[![GitHub](https://img.shields.io/badge/GitHub-manyaaa020-181717?style=flat&logo=github)](https://github.com/manyaaa020)
