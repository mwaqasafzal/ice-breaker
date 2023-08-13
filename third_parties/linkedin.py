import requests
import os

api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'

def scrape_linkedin_data(profile_url):
    """
        Given profile_url, this method scraps data from 
        provided linked-in profile.
    """
    header_dic = {'Authorization': 'Bearer ' + os.environ['PROXY_CURL']}

    response = requests.get(api_endpoint,
                        params={'url': profile_url},
                        headers=header_dic)
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in [[], '', "", None] and k not in (["people_also_viewed", "similarly_named_profiles", "recommendations", "certifications", "volunteer_work"])
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    # # TODO: Temporary, remove later
    # response = requests.get('https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json');
    # data = response.json()

    return data
