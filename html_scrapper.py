from bs4 import BeautifulSoup, SoupStrainer, PageElement, Tag
import soupsieve as sv
from requests import request

# 1. Get HTML content response using request()
test_url = 'https://github.com/airbnb'
test_response = request(method='Get',url=test_url).text
s =''

# 2. Make a soup strainer https://www.crummy.com/software/BeautifulSoup/bs4/doc/#soupstrainer
# combine dictionary with multiple items https://www.w3schools.com/python/python_dictionaries.asp
strainer_url = SoupStrainer(name=['a','span'],attrs={'itemprop': ['url', 'email','location']})

# 3. Instantiate object refer: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start
soup_obj = BeautifulSoup(test_response,'html.parser',parse_only=strainer_url)

# Create function to obtain multiple items, need too use iteration because I can't do mapping yet
for x in soup_obj.contents:
    print(x.text)