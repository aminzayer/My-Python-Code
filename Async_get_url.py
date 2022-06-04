from bs4 import BeautifulSoup
import grequests
from fake_useragent import UserAgent

urls = ['https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5396460/',
         ]

def main():
    async_list = []

    for site in urls:
        ua = UserAgent()
        action_item = grequests.get(
            site, headers={"User-Agent": ua.random}, hooks={'response': handleresponse})
        async_list.append(action_item)

    grequests.map(async_list)



def handleresponse(response, **kwargs):
    articles = BeautifulSoup(response.text, 'html.parser')
    heading_title = articles.find_all(
        'h1', class_='content-title')[0].get_text()
    print(heading_title + "\n")
    date_pubed = articles.find(
        "meta", attrs={'name': 'citation_publication_date'})['content']
    print(date_pubed)

if __name__ == '__main__':
    main()
