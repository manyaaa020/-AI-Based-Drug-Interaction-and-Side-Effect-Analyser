import pandas as pd
import os
from app.utils import clean_drug_name

# Load the dataset once on module import
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "DDI_Severity_Labeled.csv")
df = pd.read_csv(DATA_PATH)

# Normalize drug names for consistent comparison
df.rename(columns={'drug1_name': 'drug_a', 'drug2_name': 'drug_b'}, inplace=True)
df['drug_a'] = df['drug_a'].apply(clean_drug_name)
df['drug_b'] = df['drug_b'].apply(clean_drug_name)


def check_interaction(drug1, drug2):
    """
    Check if there's a known interaction between two drugs.
    Returns a dictionary with severity and description if found.
    """
    drug1 = clean_drug_name(drug1)
    drug2 = clean_drug_name(drug2)

    # Check both combinations since order may vary
    condition = (
        ((df['drug_a'] == drug1) & (df['drug_b'] == drug2)) |
        ((df['drug_a'] == drug2) & (df['drug_b'] == drug1))
    )

    result = df[condition]

    if not result.empty:
        row = result.iloc[0]
        return {
            "severity": row.get("Severity Level", "Unknown"),
            "description": row.get("interaction_type", "No description available")
        }
    else:
        return None


def get_all_interactions(drug_list):
    """
    Given a list of drugs, return all known pairwise interactions.
    Returns a DataFrame with drug pairs, severity, and description.
    """
    interactions = []

    cleaned_list = [clean_drug_name(d) for d in drug_list]

    for i in range(len(cleaned_list)):
        for j in range(i + 1, len(cleaned_list)):
            drug1 = cleaned_list[i]
            drug2 = cleaned_list[j]
            result = check_interaction(drug1, drug2)
            if result:
                interactions.append({
                    "Drug A": drug1.title(),
                    "Drug B": drug2.title(),
                    "Severity": result.get("severity", "Unknown"),
                    "Description": result.get("description", "No description available")
                })

    return pd.DataFrame(interactions)
