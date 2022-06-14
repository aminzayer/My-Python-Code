from fake_useragent import UserAgent
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

def Gathering_Links(Count,Type,TopicSubject,Datemin,Datemax):
    Search_results = []
    UA = UserAgent(use_cache_server=False)
    term = quote(TopicSubject)
    if Type.lower() == 'pubmed':
        response = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='+term+'&mindate='+Datemin+'&maxdate='+Datemax+'&retmax='+Count, headers={"User-Agent": UA.random}, timeout=(10, 30))
        infoids=BeautifulSoup(response.content, 'xml')
        ids = infoids.find_all('Id')
        for id in ids:
            Search_results.append({'Url': 'https://pubmed.ncbi.nlm.nih.gov/'+id.get_text()+'/'})
    elif Type.lower() == 'poc':
        reponse ='do somthings'
    else:
        Search_results.append(
            {'Error': 'Type not supported'})
    return Search_results



print (Gathering_Links('1000','PubMed','breast cancer','2000','2020'))
