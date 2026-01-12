import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")  # Default to gpt-3.5-turbo if not specified

# Note: API key validation happens in the LLM service when it's actually used
# This allows the server to start even if the key isn't set yet

TABLEAU_PROJECT_ID = os.getenv("TABLEAU_PROJECT_ID")
TABLEAU_PAT_NAME = os.getenv("TABLEAU_PAT_NAME")
TABLEAU_PAT_SECRET = os.getenv("TABLEAU_PAT_SECRET")
TABLEAU_SITE_ID = os.getenv("TABLEAU_SITE_ID")
TABLEAU_SERVER_URL = os.getenv("TABLEAU_SERVER_URL", "https://tableau.example.com")

TABLEAU_WORKBOOK_TEMPLATE = os.getenv("TABLEAU_WORKBOOK_TEMPLATE", "./path/to/sample_workbook.twbx")
