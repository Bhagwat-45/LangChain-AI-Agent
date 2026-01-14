from langchain.tools import tool
from todoist_api_python.api import TodoistAPI
from settings import API_Keys

@tool
def get_task():
    """
    Getting all the tasks the user has in his todoist.
    """
    print("Getting all the tasks!")
    todoist  = TodoistAPI(API_Keys.todo_api)
    tasks = []
    todo_lists = todoist.get_tasks()
    for task_list in todo_lists:
        tasks.append(task_list.content)
    return tasks    