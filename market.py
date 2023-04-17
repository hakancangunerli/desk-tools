
import yfinance as yf
import pandas as pd

def market():
    
    # get SPY500 data
    
    print("Obtaining market data...")
    
    spy_test = yf.Ticker("SPY")
    
    nas = yf.Ticker("QQQ")
    
    dji  = yf.Ticker("DIA")

    # convert pandas df to list 
    
    spy_hist = spy_test.history(period="1w")
    nas_hist = nas.history(period="1w")
    dji_hist = dji.history(period="1w")
    
    
    # empty dataframe to store data
    
    df = pd.DataFrame()
    
    # add data to dataframe
    df['Name'] =  ['SPY500', 'NASDAQ', 'DOW JONES']
    
    df['Open'] = [spy_hist['Open'][0], nas_hist['Open'][0], dji_hist['Open'][0]]
    df['Close'] = [spy_hist['Close'][0], nas_hist['Close'][0], dji_hist['Close'][0]]
    df['High'] = [spy_hist['High'][0], nas_hist['High'][0], dji_hist['High'][0]]
    df['Low'] = [spy_hist['Low'][0], nas_hist['Low'][0], dji_hist['Low'][0]]
    print(df)