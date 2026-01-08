import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")  # Default to gpt-3.5-turbo if not specified

# Note: API key validation happens in the LLM service when it's actually used
# This allows the server to start even if the key isn't set yet

