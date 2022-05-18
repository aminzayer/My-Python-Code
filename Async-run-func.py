import time
import asyncio
import requests
import aiohttp

from asgiref import sync


def timed(func):
    """
    records approximate durations of function calls
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        print('{name:<30} started'.format(name=func.__name__))
        result = func(*args, **kwargs)
        duration = "{name:<30} finished in {elapsed:.2f} seconds".format(
            name=func.__name__, elapsed=time.time() - start
        )
        print(duration)
        timed.durations.append(duration)
        return result
    return wrapper


timed.durations = []


@timed
def sync_requests_get_all(urls):
    """
    performs synchronous get requests
    """
    # use session to reduce network overhead
    session = requests.Session()
    return [session.get(url).json() for url in urls]


@timed
def async_requests_get_all(urls):
    """
    asynchronous wrapper around synchronous requests
    """
    session = requests.Session()
    # wrap requests.get into an async function

    def get(url):
        return session.get(url).json()
    async_get = sync.sync_to_async(get)

    async def get_all(urls):
        return await asyncio.gather(*[
            async_get(url) for url in urls
        ])
    # call get_all as a sync function to be used in a sync context
    return sync.async_to_sync(get_all)(urls)


@timed
def async_aiohttp_get_all(urls):
    """
    performs asynchronous get requests
    """
    async def get_all(urls):
        async with aiohttp.ClientSession() as session:
            async def fetch(url):
                async with session.get(url) as response:
                    return await response.json()
            return await asyncio.gather(*[
                fetch(url) for url in urls
            ])
    # call get_all as a sync function to be used in a sync context
    return sync.async_to_sync(get_all)(urls)


if __name__ == '__main__':
    # this endpoint takes ~3 seconds to respond,
    # so a purely synchronous implementation should take
    # little more than 30 seconds and a purely asynchronous
    # implementation should take little more than 3 seconds.
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
            'https://pubmed.ncbi.nlm.nih.gov/21969133/', ]*10

    async_aiohttp_get_all(urls)
    async_requests_get_all(urls)
    sync_requests_get_all(urls)
    print('----------------------')
    [print(duration) for duration in timed.durations]
