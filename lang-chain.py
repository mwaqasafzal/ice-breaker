from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os
from third_parties.linkedin import scrape_linkedin_data
from third_parties.twitter import scrape_user_tweets
from agents.linkdedin_lookup import get_linkedin_profile_url
from agents.twitter_lookup import get_twitter_username

load_dotenv()

if __name__ == '__main__':
#     summary_template = """
#     given the LinkedIn information {information} about a person from I want you to create:
#     1- a short summary
#     2- two interesting facts about them
# """
#     linkedin_profile_url = get_linkedin_profile_url('harrison chase')
#     linkedin_data = scrape_linkedin_data(linkedin_profile_url)

#     summary_prompt = PromptTemplate(input_variables=["information"], template=summary_template)
#     llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=os.environ['OPEN_API_KEY'])
    
#     chain = LLMChain(llm=llm, prompt=summary_prompt)
#     print(chain.run(information=linkedin_data))

      tweeter_username = get_twitter_username('Elon Musk')
      print(tweeter_username)
      tweets = scrape_user_tweets(tweeter_username)
