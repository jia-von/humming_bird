import requests
import json
import pandas as pd

# 1. Use pandas to return dataframe objects with column: url
def scrape_org(api_url):
    url = requests.get(api_url).text
    read_json = pd.read_json(url)
    return read_json['url']


# 2. This function is used to get the next link provided by GitHub Header
def link_head(api_url):
    dict_head = requests.head(api_url).links['next']
    return dict_head['url']

# 3. A function to get description, name, company, blog, location, email
def get_org_info(git_org_url):
    url = requests.get(git_org_url).text
    read_json = json.loads(url)
    final_output = pd.Series(read_json,index=['name','company','blog','location','description'])
    return final_output
    
# 4. Scrape information using HTML scrapper




