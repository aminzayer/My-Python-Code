# Import libraries
import requests
from bs4 import BeautifulSoup

page = requests.get('https://medium.com/@amin.zayeromali/about')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup)
# Pull all text from the BodyText div
Author_name = soup.find_all(
    "h2")

# Author_Followers = soup.find_all(
#   "button", class_="ca cb bl bm bn bo bp bq br bs cc cd bv ce cf")

print(Author_name)
#print(Author_Followers)
