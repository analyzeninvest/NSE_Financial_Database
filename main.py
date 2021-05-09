#!/usr/bin/env python

STOCK_TICKER_REF = "BIRET"
ALL_STOCKS = False

def main():
    """
    This is only for testing as of now.
    """
    import time, sys
    from get_stock_names_by_industry import get_all_stocks_financials_from_same_industry_of_ref, get_stock_financials
    from post_processing import fix_excel_sheet_post_download
    t0 = time.time()
    if (len(sys.argv)!=1):
        STOCK_TICKER_REF = sys.argv[1]
    if ALL_STOCKS:
        get_all_stocks_financials_from_same_industry_of_ref(STOCK_TICKER_REF)
    else:
        print("Running for: " + STOCK_TICKER_REF)
        get_stock_financials(STOCK_TICKER_REF)
    fix_excel_sheet_post_download(STOCK_TICKER_REF)
    t1 = time.time()
    t = t1 - t0
    print("Execution Time: ", t)
    
if __name__ == '__main__':
    main()

