import re
from app.interaction_checker import check_interaction
from app.utils import extract_drugs_from_text


def chatbot_response(user_input):
    """
    Process user natural language input and return an appropriate response
    about drug interactions.
    """
    drugs = extract_drugs_from_text(user_input)

    if len(drugs) < 2:
        return "❓ I need at least two drug names to check for interaction."

    drug1, drug2 = drugs[0], drugs[1]

    result = check_interaction(drug1, drug2)
    
    if result:
        response = f"⚠️ There is an interaction between **{drug1.title()}** and **{drug2.title()}**.\n\n"
        response += f"**Severity**: {result['severity']}\n"
        if result.get("description"):
            response += f"**Description**: {result['description']}"
        return response
    else:
        return f"✅ No known interaction found between **{drug1.title()}** and **{drug2.title()}** based on the database."


