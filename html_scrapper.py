from bs4 import BeautifulSoup, SoupStrainer
import soupsieve as sv
from requests import request

# 1. Get HTML content response using request()
test_url = 'https://github.com/airbnb'
test_response = request(method='Get',url=test_url).text

# Make a soup strainer https://www.crummy.com/software/BeautifulSoup/bs4/doc/#soupstrainer
# combine dictionary with multiple items https://www.w3schools.com/python/python_dictionaries.asp
strainer_url = SoupStrainer(name=['a','span'],attrs={'itemprop': ['url', 'email','location']})

# Instantiate object refer: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start
soup_obj = BeautifulSoup(test_response,'html.parser',parse_only=strainer_url)

# make a second parser with item_prop
print(soup_obj)