from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent, Tool, AgentType
import os
from tools.profile_extractor import get_profile_url

def get_twitter_username(full_name: str):
    """This method will get username of twitter profile"""
    llm = ChatOpenAI(temperature=0, openai_api_key=os.environ['OPEN_API_KEY'])
    tools = [
        Tool(
            name="Crawl Google 4 Twitter profile page",
            func=get_profile_url,
            description="useful for when you need get the Twitter Page URL"
        )
    ]

    summary = """
    given the name {full_name} I want you to find a link to their Twitter profile page, and extract from it their username.
       In Your Final answer only the person's username
       """

    prompt = PromptTemplate(input_variables=["full_name"], template=summary)
    agent = initialize_agent(llm=llm, tools=tools, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    return agent.run(prompt.format_prompt(full_name=full_name))



