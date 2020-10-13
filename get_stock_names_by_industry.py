#!/usr/bin/env python

def get_industry_of_stock(stock_ticker):
    """
    This function will fetch the industry from the list of all
    publicly traded companies.  Now for the US & India there should
    exist an xls comtaining all publicly traded company name with its
    industry.
    """
    import pandas as pd
    stock_name_industry_csv = "/home/arnashree/analyzeninvest-projects/NSE_Financial_Database/Equity-India-filtered.csv"
    stock_symbol = stock_ticker
    df_company_list = pd.read_csv(stock_name_industry_csv)
    df_stock_industry = df_company_list[df_company_list.Symbol.isin([stock_symbol])].reset_index()
    industry = df_stock_industry.loc[0, "Industry"]
    return(industry)


def get_all_peers_of_industry(industry):
    """
    This function will fetch the industry from the list of all
    publicly traded companies.  Now for the US & India there should
    exist an xls comtaining all publicly traded company name with its
    industry.
    """
    import pandas as pd
    stock_name_industry_csv = "/home/arnashree/analyzeninvest-projects/NSE_Financial_Database/Equity-India-filtered.csv"
    df_company_list = pd.read_csv(stock_name_industry_csv)
    df_industry = df_company_list[df_company_list.Industry.isin([industry])].reset_index()
    industry_peers = df_industry["Symbol"]
    #print(df_industry)
    return(industry_peers)


def get_all_stocks_financials_from_same_industry_of_ref(stock_ticker_ref):
    main_industry = get_industry_of_stock(stock_ticker_ref)
    print("Selected Industry: ", main_industry)
    all_peers = get_all_peers_of_industry(main_industry)
    print(all_peers)
    counter = 1
    for stock_ticker in all_peers:
        print("Running for: ", stock_ticker)
        print("Started " + str(counter) + " of " + str(len(all_peers)) + " stocks")
        get_stock_financials(stock_ticker)
        counter = counter + 1


def get_stock_financials(stock_ticker):
    from moneycontrol_pull_data import pull_financial_statement_from_moneycontrol
    from print_and_format_xlsx import build_dataframe_and_print_to_excel, transpose_xlsx
    stock_financials = pull_financial_statement_from_moneycontrol(stock_ticker)
    #print(stock_financials)
    build_dataframe_and_print_to_excel(stock_financials, stock_ticker)
    transpose_xlsx(stock_ticker)
        
