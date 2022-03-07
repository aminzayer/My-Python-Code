# this python file all of my function for utiliy propose
import json
import re
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from htmldate import find_date
from os.path import exists


# Use Scale SERP to Get Google Search Results & save to file
def Get_Google_Results(query, num, contry, language, domain, refresh=False):
    if (refresh == True):
        # set up the request parameters
        params = {
            'api_key': 'your api key here',
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

        #print(jsonformat)

    return jsonformat
