from bs4 import BeautifulSoup
import grequests
from fake_useragent import UserAgent
import json,re

    
def get_data_urls(page_urls):

    list_url = []
    ua = UserAgent()
    rs = (grequests.get(url['url'], headers={"User-Agent": ua.random}) for url in page_urls)
    responses = grequests.map(rs, size=5)

    i=0
    for response in responses:
        print(response)
        if response is not None:
            articles = BeautifulSoup(response.text, 'html.parser')
            heading_title = re.sub(
                '<[^<]+?>', '', articles.find('title').get_text().replace('\t', '').replace('\n', '').replace('\r', ''))
            abstract = response.content.decode('utf-8')
            date_pubed = ''
            list_url.append(page_urls[i]['id'])
            list_url.append(response.url)
            list_url.append(heading_title)
            list_url.append(abstract)
            list_url.append(date_pubed)
            i+=1

    return list_url


urls = [{'id': '6', 'url': 'https://www.mayoclinic.org/diseases-conditions/cancer/in-depth/cancer-causes/art-20044714'},
        {'id': '7', 'url': 'https://www.breastcancerfoundation.org.nz/breast-awareness/risk-factors/factors-that-dont-cause-breast-cancer'},
        {'id': '8', 'url': 'https://www.webmd.com/breast-cancer/features/sugar-and-breast-cancer'},
        {'id': '9', 'url': 'https://www.medicalnewstoday.com/articles/313490#early-signs-and-symptoms'},
         ]

urlsdata=get_data_urls(urls)

for urldata in urlsdata:
    print(urldata+"\n")


