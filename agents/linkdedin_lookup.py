from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent, Tool, AgentType
from tools.profile_extractor import get_profile_url
import os

def get_linkedin_profile_url(name: str):
    """This method will use an agent to exact url of linkedin profile"""
    template = """
            given the full name {name} I want you to get it me a link to their Linkedin profile page.
                          Your answer should contain only a URL.
    """
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", openai_api_key=os.environ['OPEN_API_KEY'])
    tools = [
        Tool(
        name='Search google for linkedin profile',
        func=get_profile_url,
        description="Use this tool to search a given linkedin profile on google"
        )
    ]

    agent = initialize_agent(llm=llm, tools=tools, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    prompt = PromptTemplate(template= template, input_variables=["name"])
    return agent.run(prompt.format_prompt(name=name))

    
