packages = ['quantstats', 'plotext', 'yfinance', 'importlib']
import importlib
import subprocess
for package in packages:
    try:
        importlib.import_module(package)
    except ImportError:
        print(f"{package} not found, installing...")
        subprocess.call(['pip', 'install', package])

import quantstats as qs 
import plotext as plt
import yfinance as yf



def line(start, end, ticker):
    plt.date_form('d/m/Y')
    start = plt.string_to_datetime(start)
    end = plt.string_to_datetime(end)
    data = yf.download(str(ticker), start, end)

    prices = list(data["Close"])
    dates = plt.datetimes_to_string(data.index)

    plt.plot(dates, prices)

    plt.title("Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Stock Price $")
    plt.show()


def candlestick(start, end, ticker):
    plt.date_form('d/m/Y')
    start = plt.string_to_datetime(start)
    end = plt.string_to_datetime(end)
    data = yf.download(str(ticker), start, end)

    dates = plt.datetimes_to_string(data.index)

    plt.candlestick(dates, data)

    plt.title("Stock Price CandleSticks")
    plt.xlabel("Date")
    plt.ylabel("Stock Price $")
    plt.show()