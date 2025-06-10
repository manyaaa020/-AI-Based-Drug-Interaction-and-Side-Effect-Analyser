import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.interaction_checker import check_interaction, get_all_interactions
from app.chatbot_engine import chatbot_response
from app.ml_predictor import predict_severity
from app.utils import clean_drug_name

st.set_page_config(page_title="Drug Interaction Checker", layout="centered")

st.title("💊 Drug Interaction Checker")

# App Tabs
tabs = st.tabs(["🔍 Interaction Search", "🤖 Chatbot", "🧠 ML Severity Predictor", "📄 Project Description"])

# -------------------------------
# 🔍 Tab 1: Manual Interaction Search
# -------------------------------
with tabs[0]:
    st.header("Search Interaction Between Two Drugs")

    drug1 = st.text_input("Enter First Drug:")
    drug2 = st.text_input("Enter Second Drug:")

    if st.button("Check Interaction"):
        if drug1 and drug2:
            result = check_interaction(drug1, drug2)
            if result:
                st.success(f"**Severity**: {result['severity']}")
                if result.get("description"):
                    st.info(f"**Description**: {result['description']}")
            else:
                st.warning("No interaction found in dataset.")
        else:
            st.error("Please enter both drug names.")

    st.markdown("---")
    st.subheader("🔗 Check All Interactions for a Drug List")
    multi_input = st.text_area("Enter a comma-separated list of drugs (e.g. Paracetamol, Ibuprofen, Aspirin)")

    if st.button("Check All Pairwise Interactions"):
        drugs = [clean_drug_name(d) for d in multi_input.split(',') if d.strip()]
        if len(drugs) < 2:
            st.warning("Enter at least two drug names.")
        else:
            interaction_df = get_all_interactions(drugs)
            if not interaction_df.empty:
                st.dataframe(interaction_df)
            else:
                st.info("No interactions found among these drugs.")

# -------------------------------
# 🤖 Tab 2: Chatbot
# -------------------------------
with tabs[1]:
    st.header("Ask About Drug Interactions")
    user_input = st.text_input("💬 Type your question (e.g., Can I take Ibuprofen and Warfarin?)")

    if st.button("Ask"):
        if user_input:
            bot_reply = chatbot_response(user_input)
            st.markdown(f"🤖 **Bot**: {bot_reply}")
        else:
            st.warning("Enter your question first.")

# -------------------------------
# 🧠 Tab 3: ML Severity Predictor (Optional)
# -------------------------------
with tabs[2]:
    st.header("Predict Severity Using Machine Learning")

    drug_a = st.text_input("Drug A")
    drug_b = st.text_input("Drug B")

    if st.button("Predict Severity"):
        if drug_a and drug_b:
            severity = predict_severity(drug_a, drug_b)
            st.success(f"Predicted Severity: {severity}")
        else:
            st.warning("Enter both drug names.")

# -------------------------------
# 📄 Tab 4: Project Description
# -------------------------------
with tabs[3]:
    st.header("💊 Drug Interaction Checker – Project Description")

    st.markdown("""
    Welcome to the **Drug Interaction Checker**, a smart AI-based tool that helps users check for possible interactions between medicines and get insights into their severity.

    ---

    ## 🧠 About the Project

    This project is designed to assist both healthcare professionals and the general public by providing a simple interface to:

    - 🔍 **Detect interactions** between two or more drugs  
    - 🚨 **Predict the severity** of those interactions using Machine Learning  
    - 📄 **Display descriptions** explaining the nature of each interaction  

    Our model was trained using labeled drug interaction datasets, and the system cross-checks user inputs against a robust database of known drug interactions.

    ---

    ## 🧰 Technologies Used

    - **Python**
    - **Streamlit** (for the interactive web app)
    - **pandas**, **scikit-learn** (for ML and data processing)
    - **Pre-trained ML models** (`pkl` files) for severity prediction
    - **Cleaned CSV datasets** of known drug interactions

    ---

    ## 🧭 How to Use the App

    From the sidebar, you can navigate to different pages:

    ### 🔹 Home  
    Check interactions between two or more drugs. Simply type in the drug names, and the system will:

    - Match them with our database
    - Display interaction severity (e.g., `major`, `moderate`, `minor`)
    - Show a brief description of the interaction

    ### 🔹 ML-Based Severity Predictor  
    Predict the severity of interaction using a trained ML model. Provide drug names, and the model outputs a predicted severity based on features.

    ### 🔹 Project Description *(This page)*  
    You're here! This page provides an overview of what the project does and how to use it.

    ---

    ## 🚀 Coming Soon

    - Upload prescriptions to auto-check interactions  
    - Explainable AI section to understand model predictions  
    - User feedback integration for better accuracy

    ---

    ## 🙋‍♀️ Created By

    """)
