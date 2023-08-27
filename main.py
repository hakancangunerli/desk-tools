
from google_search import google_search
from datetime import datetime
from organizer import organize
from market import market
from info import get_info
from ticker_finder import get_ticker
from news import news
from plots import line, candlestick
from importer import importer
print("""
  _                      _             _ 
 | |_ ___ _ __ _ __ ___ (_)_ __   __ _| |
 | __/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
 | ||  __/ |  | | | | | | | | | | (_| | |
  \__\___|_|  |_| |_| |_|_|_| |_|\__,_|_|
                                                                           
""")
# created at https://patorjk.com/software/taag/#p=display&f=Standard&t=terminal

print("Checking for package/code updates...")
importer()
def main():
    while True:
        user_input = input("► ")
        args = user_input.split()
        if 'organize' in args:
            # call the organizer py
            path_for_organizer = input(
                "Enter the path to the folder you want to organize: ")
            organize(path_for_organizer)
        if 'off' in args:
            break
        if 'time' in args:
            # got from https://www.programiz.com/python-programming/datetime/current-time
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)
        if 'news' in args:
            news()
        if 'google' in args:
            google_search()
        if 'market' in args:
            market()
        if 'tf' in args:
            ticker_to_find = input("Enter the company name: ")
            print(get_ticker(ticker_to_find))
        if 'info' in args:
            get_info()
        if 'help' in args:
            # which command do you need help with question?
            print("which command do you need help with?")
            user_help_input = input("> ")

            if 'line' in user_help_input:
                print('line  <start_date> <end_date> <ticker>')

            if 'candlestick' in user_help_input:
                print('candlestick  <start_date> <end_date> <ticker>')

        if 'line' in args:
            # check if the line(args[1], args[2], args[3]) is valid
            if len(args) != 4:
                # invalid input
                print(
                    "invalid input for line, please use the following format: line <start_date> <end_date> <ticker>")
            else:
                line(args[1], args[2], args[3])

        # same thing with candlestick
        if 'candlestick' in args:
            if len(args) != 4:
                print(
                    "invalid input, please use the following format: candlestick <start_date> <end_date> <ticker>")
            else:
                candlestick(args[1], args[2], args[3])


if __name__ == '__main__':
    main()
