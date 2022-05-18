from wsgiref import headers
import grequests
from fake_useragent import UserAgent

urls = ['https://pubmed.ncbi.nlm.nih.gov/31456179/',
        'https://pubmed.ncbi.nlm.nih.gov/20521754/',
        'https://pubmed.ncbi.nlm.nih.gov/29284222/',
        'https://pubmed.ncbi.nlm.nih.gov/15894099/',
        'https://pubmed.ncbi.nlm.nih.gov/28298516/',
        'https://pubmed.ncbi.nlm.nih.gov/24283956/',
        'https://pubmed.ncbi.nlm.nih.gov/30005774/',
        'https://pubmed.ncbi.nlm.nih.gov/28260181/',
        'https://pubmed.ncbi.nlm.nih.gov/26580154/',
        'https://pubmed.ncbi.nlm.nih.gov/28862198/',
        'https://pubmed.ncbi.nlm.nih.gov/26059925/',
        'https://pubmed.ncbi.nlm.nih.gov/28395765/',
        'https://pubmed.ncbi.nlm.nih.gov/21969133/', ]

def main():
    async_list = []

    for site in urls:
        ua = UserAgent()
        action_item = grequests.get(
            site, headers={"User-Agent": ua.random}, hooks={'response': handleresponse})
        async_list.append(action_item)

    grequests.map(async_list)



def handleresponse(response, **kwargs):
    print(response.content, kwargs)


if __name__ == '__main__':
    main()
