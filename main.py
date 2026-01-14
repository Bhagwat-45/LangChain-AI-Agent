from json import tool

from proto import Message
from settings import api_keys
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage,AIMessage
from add_task import add_task
from get_tasks import get_task
from langchain.agents import create_openai_tools_agent, AgentExecutor

tools = [add_task,get_task]

llm = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    google_api_key=api_keys.gemini_api,
    temperature=0.3,
    max_retries=0
)

system_prompt = """You are a helpful assistant. You will help the user add tasks.You will help the user to show existing tasks."""

prompt = ChatPromptTemplate([
    ("system",system_prompt),("user","{input}"), MessagesPlaceholder("agent_scratchpad"),MessagesPlaceholder("history")
    ])

agent = create_openai_tools_agent(llm,tools,prompt)

agent_executor = AgentExecutor(agent=agent,tools=tools,verbose=False)


history = []
while True:
    user_input = input("You: ")
    response = agent_executor.invoke({"input": user_input,"history": history})
    print(response)
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response["output"]))

