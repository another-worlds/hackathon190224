from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, ChatMessagePromptTemplate
from langchain_core.messages import ChatMessage
from langchain_openai import ChatOpenAI

# load .env
load_dotenv()

# initialize prompt from messages:
system_message_text = """you are a {role} who uses internal documents to provide users with answers to their queries. 
               If no relevant context is provided, kindly ask customer if you can help with something else.
            """

role = "helpful assistant"

base_prompt = PromptTemplate.from_template(system_message_text)

chat = ChatOpenAI(temperature=0.1)
chain = base_prompt | chat

answer = chain.invoke({"role": role})
print(answer)

