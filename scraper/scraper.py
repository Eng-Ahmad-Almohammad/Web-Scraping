import requests 
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    final_result =[]
    data = requests.get(url)
    soup = BeautifulSoup(data.content , 'html.parser')
    page_span = soup.find_all('span')
    
    for i in page_span:
        if i.text == 'citation needed':
            final_result.append(i)
    
    
    return len(final_result)



def get_citations_needed_report(url):
    final_result = []
    data = requests.get(url)
    soup = BeautifulSoup(data.content ,'html.parser' )
    page_p = soup.findAll('p')
    for p in page_p:
        if p.findChildren('span' , recursive=True):
            final_result.append(p.text)

    for i in final_result:
        print(i)

print(get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico"))
get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")