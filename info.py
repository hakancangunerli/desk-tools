import quantstats as qs

from ticker_finder import get_ticker


from terminaltables import AsciiTable

def get_info():
    # select an action to perform

    name_of_company = str(get_ticker(input("Enter the name of the company: ")))

    selection = int(input("""Select which action you'd like to perform using guide below
                        [1] : Monthly Returns  
                        [2] : Profit Ratio
                        [3] Volatility
                        [4] General Report:"""
                        ))

    tick = qs.utils.download_returns(get_ticker(name_of_company))

    # # write a switch statement to select which action to perform

    if selection == 1: 
        # print monthly heatmap 
        print(qs.stats.monthly_returns(tick))
            
    if selection == 2:
        print(f"The profit ratio for {name_of_company} is:",qs.stats.profit_ratio(tick))

    if selection == 3:
        print(f"The volatility for {name_of_company} is:", qs.stats.volatility(tick))

    if selection == 4:
        # FIXME: give them a full report
        print(qs.reports.html(tick, output='report.html', title='Report'))

    # NOTE: yahoofinancials could also be viable here



