import re
import pandas as pd

def clean_drug_name(name):
    """
    Standardizes drug names for consistent comparisons.
    Removes extra spaces and lowercases everything.
    """
    return name.strip().lower()


def extract_drugs_from_text(text):
    """
    Extracts potential drug names from user input.
    Assumes drug names are capitalized words or known terms.
    You can enhance this using spaCy or a known drug list.
    """
    # Basic version: grab capitalized words
    possible_drugs = re.findall(r'\b[A-Z][a-zA-Z]+\b', text)
    return [clean_drug_name(word) for word in possible_drugs]


def load_unique_drugs(df):
    """
    Returns a sorted list of all unique drugs in the dataset.
    Useful for dropdowns or autocomplete UIs.
    """
    drugs = pd.concat([df['drug_a'], df['drug_b']])
    unique = sorted(drugs.str.lower().str.strip().unique())
    return unique
