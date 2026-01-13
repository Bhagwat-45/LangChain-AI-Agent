import os
from dotenv import load_dotenv

load_dotenv()

class API_Keys():
    todo_api = os.getenv("TODOIST_API_KEY")
    gemini_api = os.getenv("GEMINI_API_KEY")

api_keys = API_Keys()