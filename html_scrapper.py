from pprint import PrettyPrinter
from bs4 import BeautifulSoup
from requests import request

# 1. Get HTML content response using request()

test_url = 'https://github.com/pandas-dev/'
test_response = request(method='Get',url=test_url).text

# Instantiate object refer: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start
soup_obj = BeautifulSoup(test_response,'html.parser')

# Using beautiful soup to get org email, location, url link, and social media
# Use CSS-Selector: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors
soup_org_details = soup_obj.select('div.flex-1:nth-child(2) > div:nth-child(3)')

print(soup_org_details)