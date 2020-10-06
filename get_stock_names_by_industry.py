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
