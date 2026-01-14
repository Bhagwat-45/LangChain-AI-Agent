from langchain.tools import tool
from todoist_api_python.api import TodoistAPI
from settings import API_Keys

@tool
def add_task(task:str,description:str=None):
    """
    Add a new task to the user's task list. Use this when they need to add the task
    """
    print(f"Adding Task : {task}")
    todoist = TodoistAPI(API_Keys.todo_api)
    todoist.add_task(content=task,description=description)
    print("Task Added")

