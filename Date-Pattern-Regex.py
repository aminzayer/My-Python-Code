from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import grequests
from htmldate import find_date
import datetime

my_links = ['https://www.breastcancer.org/facts-statistics/myths-vs-facts', 'https://breastcancernow.org/information-support/have-i-got-breast-cancer/breast-cancer-causes/10-common-breast-cancer-myths-dispelled', 'https://www.webmd.com/cancer/brain-cancer/features/vitamins-supplements-breast-cancer-treatment', 'https://www.breastcancer.org/risk/risk-factors/family-history', 'https://www.breastcancerfoundation.org.nz/breast-awareness/risk-factors/factors-that-dont-cause-breast-cancer', 'https://www.gavi.org/vaccineswork/will-mrna-vaccine-alter-my-dna', 'https://www.cdc.gov/media/releases/2021/s0811-vaccine-safe-pregnant.html', 'https://health.clevelandclinic.org/what-happens-if-you-miss-your-second-covid-vaccine/', 'https://www.cancer.ca/en/prevention-and-screening/reduce-cancer-risk/make-informed-decisions/myths-and-controversies/bras/?region=on', 'https://www.breastcancer.org/risk/factors/no_evidence', 'https://www.center4research.org/can-wearing-bra-cause-breast-cancer/', 'https://www.health.harvard.edu/blog/myth-busted-bra-wearing-not-linked-breast-cancer-201409097391', 'https://www.sciencedaily.com/releases/2014/09/140905090615.htm', 'https://www.mayoclinic.org/diseases-conditions/cancer/in-depth/cancer-causes/art-20044714https://www.cancer.ca/en/prevention-and-screening/reduce-cancer-risk/make-informed-decisions/myths-and-controversies/antiperspirants-parabens/?region=on', 'https://breastcancernow.org/information-support/have-i-got-breast-cancer/breast-cancer-causes/10-common-breast-cancer-myths-dispelled#deodorant', 'https://www.cancerwa.asn.au/resources/cancermyths/deodorants-breast-myth/', 'https://www.breastcancer.org/symptoms/understand_bc/myths-facts', 'https://www.webmd.com/breast-cancer/features/sugar-and-breast-cancer', 'https://www.medicalnewstoday.com/articles/313490#early-signs-and-symptoms', 'https://www.cancercenter.com/cancer-types/breast-cancer/symptoms', 'https://www.cdc.gov/cancer/breast/basic_info/treatment.htm', 'https://www.cancer.org/cancer/breast-cancer/treatment/', 'https://www.bayer.com/en/news-stories/5-myths-about-breast-cancer', 'https://www.webmd.com/breast-cancer/features/life-after-breast-cancer-treatment', 'https://www.cancer.net/cancer-types/breast-cancer/follow-care-and-monitoring', 'https://www.nationalbreastcancer.org/breast-cancer-myths/',
            'https://www.aetna.com/health-guide/breast-cancer-myths.html', 'http://www.bccancer.bc.ca/screening/breast/breast-health/facts-myths', 'https://www.nationalbreastcancer.org/breast-cancer-myths/a-mammogram-can-cause-breast-cancer-to-spread/', 'https://www.cancer.org/cancer/cancer-causes/is-cancer-contagious.html', 'https://www.cancer.org/cancer/breast-cancer/screening-tests-and-early-detection/mammograms/mammograms-for-women-with-breast-implants.html', 'https://cancer.stonybrookmedicine.edu/breast-cancer-team/patients/bse/breastlumps', 'https://www.webmd.com/breast-cancer/features/breast-lumps-8-myths-and-facts', 'https://www.healthline.com/health/breast-cancer/does-coffee-increase-risk', 'https://www.breastcancer.org/research-news/hair-dye-and-straighteners-linked-to-higher-riskhttps://www.cancer.org/latest-news/how-your-weight-affects-your-risk-of-breast-cancer.html', 'https://www.cancer.gov/about-cancer/causes-prevention/risk/radiation/electromagnetic-fields-fact-sheet', 'https://breastcancernow.org/information-support/have-i-got-breast-cancer/breast-cancer-causes/10-common-breast-cancer-myths-dispelled#piercing', 'https://www.cancer.gov/about-cancer/causes-prevention/risk/myths', 'https://www.maurerfoundation.org/can-nipple-piercings-increase-your-risk-of-breast-cancer/', 'https://www.verywellhealth.com/nipple-piercing-health-risks-513608', 'https://www.breastcancer.org/risk/factors/family_history', 'https://www.maurerfoundation.org/estrogen-and-breast-cancer/', 'https://www.cancer.gov/about-cancer/causes-prevention/risk/hormones', 'https://www.healthline.com/health-news/dairy-products-and-breast-cancer-risk', 'https://www.cancer.org/cancer/breast-cancer/screening-tests-and-early-detection/mammograms/limitations-of-mammograms.html', 'https://www.mayoclinic.org/healthy-lifestyle/womens-health/in-depth/breast-cancer-prevention/art-20044676', 'https://www.nationalbreastcancer.org/breast-cancer-myths/','https://www.bayer.com/en/news-stories/5-myths-about-breast-cancer', 'https://www.hopkinsmedicine.org/kimmel_cancer_center/cancers_we_treat/breast_cancer_program/treatment_and_services/survivorship/myths.html', 'https://www.breastcancer.org/risk/risk-factors/low-vitamin-d-levels', 'https://www.breastcancer.org/managing-life/diet-nutrition/dietary-supplements/known/vitamin-c']


# Get the date from the text
def Parallel_Fetching_Link_Data(urls):
    Url_list = []
    for url in urls:
        UA = UserAgent(cache=True, use_cache_server=True,
                       fallback='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', verify_ssl=False)
        url_data_response = grequests.get(
            url, headers={"User-Agent": UA.random}, hooks={'response': Handel_Response_Fetcheing},  timeout=(100, 300), verify=False)
        Url_list.append(url_data_response)

    grequests.map(
        Url_list, exception_handler=Exception_Handel_Response_Fetcheing, size=100)


def Handel_Response_Fetcheing(response, **kwargs):
    articles = BeautifulSoup(response.text, 'html.parser')
    heading_title = articles.find_all('h1')[0].get_text()
    heading_title = " ".join(heading_title.split())
    #clean_text = " ".join(articles.getText().split())
    date_article = find_date(str(response.content), extensive_search=True,
                             original_date=True, outputformat='%m/%d/%Y')
    date_float = datetime.datetime.timestamp(
        datetime.datetime.strptime(date_article, '%Y-%m-%d'))
    print("\n")
    print("URL:", response.url)
    print("Title:", heading_title)
    #print("clean_text:", clean_text)
    print("Last Update (Date Format):", date_article)
    print("Last Update (Float Format):", date_float)


def Exception_Handel_Response_Fetcheing(request, exception):
    print("\n\n", request.url, "\nError: ", exception)


print(len(my_links))
Parallel_Fetching_Link_Data(my_links)
