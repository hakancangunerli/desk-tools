url = 'https://finviz.com/news.ashx'

# the table is at div class = news 
import importlib
packages = ['bs4', 'urllib.request', 'subprocess']

for package in packages:
    try:
        importlib.import_module(package)
    except ImportError:
        print(f"{package} not found, installing...")
        subprocess.call(['pip', 'install', package])

print("Check complete")
        
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd 

def news():
    
    req = Request(url=url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}) 
    response = urlopen(req)    
    # Read the contents of the file into 'html'
    html = BeautifulSoup(response, features = 'lxml')
    
    # table is in a div with an id of news, # get the table with the class table-fixed
    table = html.find('div', {'id': 'news'}).find('table', {'class': 'table-fixed'})
    
    dfs = []

    for i in range(10):
        # create a new DataFrame for each iteration
        new_df = pd.DataFrame({'Date': table.find_all('tr')[i].find_all('td')[1].text,
                            'Headline': table.find_all('tr')[i].find_all('td')[2].text},
                            index=[i])
        # append the new DataFrame to the list
        dfs.append(new_df)
        
    # concatenate all DataFrames in the list into a single DataFrame
    df = pd.concat(dfs)

    # now, remove the rows that contain the text 'Loading...'
    df = df[~df['Headline'].str.contains('Loading')]

    # print it similar to the original above
    for i in range(len(df)):
        print(df.iloc[i,0], df.iloc[i,1])

