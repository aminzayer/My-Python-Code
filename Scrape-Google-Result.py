import urllib
from fake_useragent import UserAgent
import requests
import re
from bs4 import BeautifulSoup

keyword = "Amin Zayeromali"
html_keyword = urllib.parse.quote_plus(keyword)
print(html_keyword)

google_url = "https://www.google.com/search?q=" + html_keyword 
print(google_url)

ua = UserAgent()
response = requests.get(google_url, {"User-Agent": ua.random})
soup = BeautifulSoup(response.text, "html.parser")

result = soup.find_all('div', attrs={'class': 'ZINbbc'})
results = [re.search('\/url\?q\=(.*)\&sa', str(i.find('a', href=True)['href']))
           for i in result if "url" in str(i)]
#this is because in rare cases we can't get the urls
links = [i.group(1) for i in results if i != None]
#print(links)

print(soup.prettify())
