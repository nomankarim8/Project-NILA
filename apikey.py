import os

API_KEY = os.getenv("OPENAI_API_KEY")
api_data = API_KEY or ""


def get_api_key():
    return api_data or os.getenv("OPENAI_API_KEY", "")
 