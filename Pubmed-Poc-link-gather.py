from fake_useragent import UserAgent
import requests,json
from urllib.parse import quote
from bs4 import BeautifulSoup


def Gathering_Links(Count, Type, TopicSubject, Datemin, Datemax):
    Search_results = []
    UA = UserAgent(use_cache_server=False)
    term = quote(TopicSubject)
    if Type.lower() == 'pubmed':
        try:
            response = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='+term +
                                    '&mindate='+Datemin+'&maxdate='+Datemax+'&retmax='+Count, headers={"User-Agent": UA.random}, timeout=(10, 30))
            infoids = BeautifulSoup(response.content, 'xml')
            ids = infoids.find_all('Id')
            for id in ids:
                Search_results.append(
                    {'Url': 'https://pubmed.ncbi.nlm.nih.gov/'+id.get_text()+'/'})
        except:
            Search_results.append({'Error': 'Error raised in Request'})
    elif Type.lower() == 'poc':
        try:
            articles = requests.get(
                'https://secureapi.atpoc.com/api-contentstream/beta/factually/', headers={"User-Agent": UA.random}).json()
            for article in articles.values():
                Search_results.append(
                    {'Url': 'https://breakingmed.org/article.html?articleid=' + article['articleid']})
        except Exception as e:
            Search_results.append({'Error': str(e)})
    else:
        Search_results.append({'Error': 'Type not supported'})
    return Search_results


print(Gathering_Links('100', 'poc', 'breast cancer', '2000', '2020'))
