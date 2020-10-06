#!/usr/bin/env python

STOCK_TICKER_REF = "BDL"

def main():
    """
    This is only for testing as of now.
    """
    from moneycontrol_pull_data import pull_financial_statement_from_moneycontrol
    from print_and_format_xlsx import build_dataframe_and_print_to_excel, transpose_xlsx
    from get_stock_names_by_industry import get_all_peers_of_industry, get_industry_of_stock
    import time
    t0 = time.time()
    main_industry = get_industry_of_stock(STOCK_TICKER_REF)
    all_peers = get_all_peers_of_industry(main_industry)
    counter = 1
    for stock_ticker in all_peers:
        print("Running for: ", stock_ticker)
        print("Started " + str(counter) + " of " + str(len(all_peers)) + " stocks")
        stock_financials = pull_financial_statement_from_moneycontrol(stock_ticker)
        build_dataframe_and_print_to_excel(stock_financials, stock_ticker)
        transpose_xlsx(stock_ticker)
        #print(stock_financials)
        t1 = time.time()
        t = t1 - t0
        print("Execution Time: ", t)
    
if __name__ == '__main__':
    main()

