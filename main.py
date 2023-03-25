from plots import line, candlestick
import os 
from news import news


# you pass in args as start, end, ticker, and the type of graph (line, candlestick)

def test():
    args = os.sys.argv
    if args[1] == 'news':
        news()
        exit(0)
    if args[4] == 'line':
        line(args[1], args[2], args[3])
    if args[4] == 'candlestick':
        candlestick(args[1], args[2], args[3])
test()