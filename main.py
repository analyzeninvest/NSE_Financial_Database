#!/usr/bin/env python

STOCK_TICKER_REF = "HEG"

def main():
    """
    This is only for testing as of now.
    """
    import time
    from get_stock_names_by_industry import get_all_stocks_financials_from_same_industry_of_ref, get_stock_financials
    t0 = time.time()
    get_all_stocks_financials_from_same_industry_of_ref(STOCK_TICKER_REF)
    #get_stock_financials(STOCK_TICKER_REF)
    t1 = time.time()
    t = t1 - t0
    print("Execution Time: ", t)
    
if __name__ == '__main__':
    main()

