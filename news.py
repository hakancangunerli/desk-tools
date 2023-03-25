
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
url = 'https://finviz.com/news.ashx'

# the table is at div class = news 

def news():
    req = Request(url=url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}) 
    response = urlopen(req)    
    # Read the contents of the file into 'html'
    html = BeautifulSoup(response, features = 'lxml')
    
    # table is in a div with an id of news, # get the table with the class table-fixed
    table = html.find('div', {'id': 'news'}).find('table', {'class': 'table-fixed'})
    
    # FIXME: need to remove the 'Loading...' ones.

    # print the first 10 rows of the table, if it says loading, then don't show that tr and td
    for i in range(10):
          print(table.find_all('tr')[i].find_all('td')[1].text, table.find_all('tr')[i].find_all('td')[2].text)  
            
    
    
    
news()