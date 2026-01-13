from settings import api_keys
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=api_keys.gemini_api,
    temperature=0.3
)


system_prompt = "You are a helpful assistant. You will help the user add tasks."
user_input = "Tell me best way to manage my time ?"

prompt = ChatPromptTemplate([
    ("system",system_prompt),("user",user_input)
    ])

chain = prompt | llm | StrOutputParser()

responses = chain.invoke({"input": user_input})

print(responses)