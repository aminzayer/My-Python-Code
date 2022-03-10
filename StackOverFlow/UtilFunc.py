# this python file all of my function for utiliy propose
import json
import re
import os
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from htmldate import find_date
from os.path import exists
from django.conf import settings

# Use Scale SERP to Get Google Search Results & save to file
def Get_Google_Results(query, num, contry, language, domain, refresh=False):
    if (refresh == True):
        # set up the request parameters
        params = {
            'api_key': 'E2645AF134164B22BF070B76BA4732B5',  # api key for Scale Serep Service
            'q': query,
            'num': num,
            'gl': contry,
            'hl': language,
            'google_domain': domain
        }

        # make the http GET request to Scale SERP
        api_result = requests.get('https://api.scaleserp.com/search', params)

        # convert to the JSON response from Scale SERP
        jsonformat = json.dumps(api_result.json())

    return jsonformat

# Removing All tag and give clean text of links
def beautifulsoup_extract_text(response_content):
    # Create the beautifulsoup object:
    soup = BeautifulSoup(response_content, 'html.parser')

    # Finding the text:
    text = soup.find_all(text=True)

    # Remove unwanted tag elements:
    cleaned_text = ''
    blacklist = ['[document]', 'noscript', 'header', 'html',
                 'meta', 'head', 'input', 'script', 'style', 'footer', ]

    # Then we will loop over every item in the extract text and make sure that the beautifulsoup4 tag
    # is NOT in the blacklist
    for item in text:
        if item.parent.name not in blacklist:
            cleaned_text += '{} '.format(item)

    # remove all of remianed html tag
    cleaned_text = re.sub('<[^<]+?>', '', cleaned_text)

    # remove all of text links
    cleaned_text = re.sub(r'http\S+', '', cleaned_text)

    # Remove any tab separation and strip the text:
    cleaned_text = cleaned_text.replace('\t', '')

    return cleaned_text.strip()

# Collect Links and getting clean Text
def collect_link(query, language, num_fetch, num, country, force_refresh=False):
    # Step 1 : Collecting Links and getting clean Text.
    # Caching section of web service results to temp file
    # Temp file full name & path
    temp_file_name = os.path.join(
        settings.BASE_DIR, 'Temp') + '/google_results.json'

    # force refresh : delete temp caching file
    if force_refresh == True:
        if exists(temp_file_name):
            os.remove(temp_file_name)

    # Check Temp Caching file is exist
    if not exists(temp_file_name):
        Results = Get_Google_Results(query, num=num_fetch+1, contry=country,
                                     language=language, domain='google.com', refresh=True)
        with open(temp_file_name, 'w') as f:
            json.dump(Results, f)

    # Step 2 : Get the full text of the links collected from Google
    # Load Links from Json Temp file Caching
    with open(temp_file_name) as json_file:
        google_result_data = json.load(json_file)

    # Step 2 : Get the full text of the links collected from Google
    Search_data = json.loads(google_result_data)

    # Database Structure
    Collectedlink = []

    # Collectlink Structure
    # {
    #     'linkid': '',
    #     'article_link': '',
    #     'summary_link': '',
    #     'posted_date': '',
    #     'text_link': '',
    # }

    # fetching all link text and save to Collectlink Dictionary
    count = 1
    for i in range(80):
        try:
            # Get Html of links and cleaning
            response = requests.get(
                Search_data["organic_results"][i]["link"], timeout=10)
            doc_html = response.content.decode('utf8')
            # check posted date of links from google result is exist
            date_match=[]
            if "date" in Search_data["organic_results"][i]:
                date_match = re.findall(r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2},\s\d{4}', Search_data["organic_results"][i]["date"])

            if len(date_match) == 1:
                posted_date = date_match[0]
            else:
                # If the posted date does not exist, it will fetch the date link itself
                posted_date = str(find_date(
                    Search_data["organic_results"][i]["link"], extensive_search=True, original_date=True, outputformat="%b %-d, %Y"))
                # If it does not find any date, it will set the download date
                if posted_date == '' or posted_date is None or posted_date == 'None':
                    posted_date = datetime.now().strftime("%b %-d, %Y")

            # cleaning html and only get text
            doc_text = beautifulsoup_extract_text(doc_html)

            # insert link data to array of Collectlink Dictionary
            doc_text = ' '.join(doc_text.split())
            Collectedlink.append(
                {'linkid': count, 'article_link': Search_data["organic_results"][i]["link"], 'summary_link': Search_data["organic_results"][i]["snippet"], 'posted_date': posted_date, 'text_link': doc_text})

            # outputing operation on terminal
            print("Link of ", i, " received - Total Count :", count)
            count += 1

            # Only 50 of correct link for this Task
            if count > num + 1:
                break
        except ValueError:
            print("Link of ", i, " Not received - Error =",
                  ValueError, " - Total Count :", count)
            pass
        except requests.Timeout:
            # if Timeout continue fetching
            pass
        except requests.ConnectionError:
            # if ConnectionError fetching
            pass

    # Return All Collected Links data
    return Collectedlink
