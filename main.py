#!/usr/bin/env python

def main():
    """
    This is only for testing as of now.
    """
    #cash_flow = pull_cash_flow_statement_from_moenyontrol('TCS')
    #print(cash_flow)
    #print(get_url_of_moneycontrol_from_ticker('TCS', "cash flow"))
    #print(google_moneycontrol_base_sitename('TCS'))
    from moneycontrol_pull_data import pull_financial_statement_from_moneycontrol
    from print_and_format_xlsx import build_dataframe_and_print_to_excel
    import time
    t0 = time.time()
    stock_ticker = 'HINDZINC'
    stock_financials = pull_financial_statement_from_moneycontrol(stock_ticker)
    #stock_financials = pull_profit_and_loss_statement_from_moneycontrol(stock_ticker)
    #print(stock_financials)
    build_dataframe_and_print_to_excel(stock_financials, stock_ticker)
    #print(stock_financials)
    t1 = time.time()
    t = t1 - t0
    print("Execution Time: ", t)
    #d1 = {"a":[1, 2, 3], "b":[11, 12, 13], "c":[0]}
    #d2 = {"a":[4, 5, 6], "b":[111, 112, 113, 114], "d": [100]}
    #print(merge_array_of_2_dictionary_with_same_key(d1, d2))
    #PnL = pull_profit_and_loss_statement_from_moneycontrol('TCS')
    #print(PnL)
    
if __name__ == '__main__':
    main()

