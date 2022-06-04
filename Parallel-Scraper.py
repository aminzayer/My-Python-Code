from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import grequests

my_links = ['https://pubmed.ncbi.nlm.nih.gov/31456179/',
            'https://pubmed.ncbi.nlm.nih.gov/20521754/',
            'https://pubmed.ncbi.nlm.nih.gov/29284222/',
            'https://pubmed.ncbi.nlm.nih.gov/15894099/',]


# Get the date from the text
def Parallel_Fetching_Link_Data(urls):
    # Pubmed link data structure
    LinksData = {'Error': 'OK', 'title': '', 'abstract': '', 'PostedDate': ''}
    Url_list = []
    for url in urls:
        ua = UserAgent()
        url_data_response = grequests.get(
            url, headers={"User-Agent": ua.random}, hooks={'response': Handel_Response_Fetcheing})
        Url_list.append(url_data_response)

    grequests.map(
        Url_list, exception_handler=Exception_Handel_Response_Fetcheing, size=100)


def Handel_Response_Fetcheing(response, **kwargs):
    articles = BeautifulSoup(response.text, 'html.parser')
    heading_title = articles.find_all('h1')[0].get_text()
    heading_title = " ".join(heading_title.split())
    abstract = articles.find_all(
        'div', class_='abstract-content selected')[0].get_text().replace('\t', '')
    abstract = " ".join(abstract.split())
    print("\n")
    print("URL:", response.url)
    print("Title:", heading_title)
    print("Abstract:", abstract)


def Exception_Handel_Response_Fetcheing(request, exception):
    print("\n\n", request.url, "\nError: ", exception)


Parallel_Fetching_Link_Data(my_links)