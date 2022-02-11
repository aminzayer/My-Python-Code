# Import libraries
import re
import requests
from bs4 import BeautifulSoup

page = requests.get('https://medium.com/@amin.zayeromali')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup)
# Pull all text from the BodyText div
Author_Followers = soup.find("button").getText()
Author_Stories = soup.find_all("article")

print(Author_Followers)
print(len(Author_Stories))
