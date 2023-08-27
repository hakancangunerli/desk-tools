

# This code is from a GH Gist by @bruhbruhroblox
#https://gist.github.com/bruhbruhroblox/dd9d981c8c37983f61e423a45085e063
import importlib

packages = ['requests']

for package in packages:
    try:
        importlib.import_module(package)
    except ImportError:
        print(f"{package} not found, installing...")
        subprocess.call(['pip', 'install', package])
    
def get_ticker(company_name):
    import requests # this is necessary as it's used as an access for get requests
    yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    params = {"q": company_name, "quotes_count": 1, "country": "United States"}

    res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
    data = res.json()

    company_code = data['quotes'][0]['symbol']
    return company_code
