# app/__init__.py

# Initialize package and import main functionalities
from .interaction_checker import check_interaction, get_all_interactions
from .chatbot_engine import chatbot_response
from .ml_predictor import predict_severity
from .utils import clean_drug_name
