#!/usr/bin/env python

def pull_financial_statement_from_moneycontrol(stock_ticker):
    """
    This Function will pull all the Financial statements from the moneycontrol website.
    Target Pages are: 
    1. Profit & Loss / Income Statement
    2. Balance Sheet
    3. Cash Flow Statement
    4. Key Ratios
    Final Output will be a dictionary. 
    """
    profit_and_loss_stateents = pull_profit_and_loss_statement_from_moneycontrol(stock_ticker)
    balance_sheets = pull_balance_sheet_from_moenycontrol(stock_ticker)
    cash_flow_statements = pull_cash_flow_statement_from_moenyontrol(stock_ticker)
    ratios = pull_key_ratios_from_moneycontrol(stock_ticker)
    financials = {"Profit and Loss Statement": profit_and_loss_stateents,
                  "Balance Sheet" : balance_sheets,
                  "Cash Flow" : cash_flow_statements,
                  "Key Ratios" : ratios
                  }
    return(financials)

def merge_array_of_2_dictionary_with_same_key(dict1, dict2):
    """
    Merge Dict1 & Dict2 into a single one if keys are same.
    Returns a dict.
    """
    merged_dict = {}
    for key1 in dict1:
        merged_array = []
        for key2 in dict2:
            if key1 == key2 :
                if isinstance(dict2.get(key2), list):
                    merged_array = dict1.get(key1) + dict2.get(key2)
                    merged_dict[key2] = merged_array
                else:
                    merged_dict[key2] = dict2.get(key2)
    return(merged_dict)
                
def pull_profit_and_loss_statement_from_moneycontrol(stock_ticker):
    """
    This Function will pull the Financial statements from the moneycontrol website.
    Target Pages is Profit & Loss / Income Statement
    Final Output will be a dictionary. 
    """
    all_urls = get_url_of_moneycontrol_from_ticker(stock_ticker, "income statement")
    standalone_profit_and_loss_statement_current_page = []
    consolidated_profit_and_loss_statement_current_page = []
    for url in all_urls["standalone"]:
        standalone_profit_and_loss_statement_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    for url in all_urls["consolidated"]:
        consolidated_profit_and_loss_statement_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    standalone_profit_and_loss_statement = merge_array_of_2_dictionary_with_same_key(
        merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                standalone_profit_and_loss_statement_current_page[0],
                standalone_profit_and_loss_statement_current_page[1]),
            standalone_profit_and_loss_statement_current_page[2]),
        standalone_profit_and_loss_statement_current_page[3])
    consolidated_profit_and_loss_statement = merge_array_of_2_dictionary_with_same_key(
        merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                consolidated_profit_and_loss_statement_current_page[0],
                consolidated_profit_and_loss_statement_current_page[1]),
            consolidated_profit_and_loss_statement_current_page[2]),
        consolidated_profit_and_loss_statement_current_page[3])
    profit_and_loss_statements = {"Standalone" : standalone_profit_and_loss_statement, "Consolidated" : consolidated_profit_and_loss_statement}
    return(profit_and_loss_statements)

def pull_balance_sheet_from_moenycontrol(stock_ticker):
    """
    This Function will pull the Financial statements from the moneycontrol website.
    Target Pages is Balance Sheet
    Final Output will be a dictionary. 
    """
    all_urls = get_url_of_moneycontrol_from_ticker(stock_ticker, "balance sheet")
    standalone_balance_sheet_current_page = []
    consolidated_balance_sheet_current_page = []
    for url in all_urls["standalone"]:
        standalone_balance_sheet_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    for url in all_urls["consolidated"]:
        consolidated_balance_sheet_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    standalone_balance_sheet = merge_array_of_2_dictionary_with_same_key(
        merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                standalone_balance_sheet_current_page[0],
                standalone_balance_sheet_current_page[1]),
            standalone_balance_sheet_current_page[2]),
        standalone_balance_sheet_current_page[3])
    consolidated_balance_sheet = merge_array_of_2_dictionary_with_same_key(
        merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                consolidated_balance_sheet_current_page[0],
                consolidated_balance_sheet_current_page[1]),
            consolidated_balance_sheet_current_page[2]),
        consolidated_balance_sheet_current_page[3])
    balance_sheets = {"Standalone" : standalone_balance_sheet, "Consolidated" : consolidated_balance_sheet}
    return(balance_sheets)

def pull_cash_flow_statement_from_moenyontrol(stock_ticker):
    """
    This Function will pull the Financial statements from the moneycontrol website.
    Target Pages is Cash Flow Statement
    Final Output will be a dictionary. 
    """
    all_urls = get_url_of_moneycontrol_from_ticker(stock_ticker, "cash flow")
    standalone_cash_flow_statement_current_page = []
    consolidated_cash_flow_statement_current_page = []
    for url in all_urls["standalone"]:
        standalone_cash_flow_statement_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    for url in all_urls["consolidated"]:
        consolidated_cash_flow_statement_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    standalone_cash_flow_statement = merge_array_of_2_dictionary_with_same_key(
        merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                standalone_cash_flow_statement_current_page[0],
                standalone_cash_flow_statement_current_page[1]),
            standalone_cash_flow_statement_current_page[2]),
        standalone_cash_flow_statement_current_page[3])
    consolidated_cash_flow_statement = merge_array_of_2_dictionary_with_same_key(
        merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                consolidated_cash_flow_statement_current_page[0],
                consolidated_cash_flow_statement_current_page[1]),
            consolidated_cash_flow_statement_current_page[2]),
        consolidated_cash_flow_statement_current_page[3])
    cash_flow_statements = {"Standalone" : standalone_cash_flow_statement, "Consolidated" : consolidated_cash_flow_statement}
    return(cash_flow_statements)

def pull_key_ratios_from_moneycontrol(stock_ticker):
    """
    This Function will pull the Financial statements from the moneycontrol website.
    Target Pages is Key Ratios
    Final Output will be a dictionary. 
    """
    all_urls = get_url_of_moneycontrol_from_ticker(stock_ticker, "ratios")
    standalone_ratios_current_page = []
    consolidated_ratios_current_page = []
    for url in all_urls["standalone"]:
        standalone_ratios_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    for url in all_urls["consolidated"]:
        consolidated_ratios_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    standalone_ratios = merge_array_of_2_dictionary_with_same_key(
        merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                standalone_ratios_current_page[0],
                standalone_ratios_current_page[1]),
            standalone_ratios_current_page[2]),
        standalone_ratios_current_page[3])
    consolidated_ratios = merge_array_of_2_dictionary_with_same_key(
        merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                consolidated_ratios_current_page[0],
                consolidated_ratios_current_page[1]),
            consolidated_ratios_current_page[2]),
        consolidated_ratios_current_page[3])
    ratios = {"Standalone" : standalone_ratios, "Consolidated" : consolidated_ratios}
    #print(ratios)
    return(ratios)

def get_url_of_moneycontrol_from_ticker(stock_ticker, financial_type):
    """
    This function will get the URL for the stock of moneycontrol website. Both consolidated & standalone pages will be given up to max 20 years.
    Final Output will be the URL as a dictionary.
    """
    base_url, MC_ticker = google_moneycontrol_base_sitename(stock_ticker)
    if financial_type == "balance sheet":
        standalone_url1 = base_url + 'balance-sheetVI/'+ MC_ticker +'/#' + MC_ticker
        standalone_url2 = base_url + 'balance-sheetVI/'+ MC_ticker +'/2#' + MC_ticker
        standalone_url3 = base_url + 'balance-sheetVI/'+ MC_ticker +'/3#' + MC_ticker
        standalone_url4 = base_url + 'balance-sheetVI/'+ MC_ticker +'/4#' + MC_ticker
        consolidated_url1 = base_url + 'consolidated-balance-sheetVI/'+ MC_ticker +'/#' + MC_ticker
        consolidated_url2 = base_url + 'consolidated-balance-sheetVI/'+ MC_ticker +'/2#' + MC_ticker
        consolidated_url3 = base_url + 'consolidated-balance-sheetVI/'+ MC_ticker +'/3#' + MC_ticker
        consolidated_url4 = base_url + 'consolidated-balance-sheetVI/'+ MC_ticker +'/4#' + MC_ticker
    elif financial_type == "income statement":
        standalone_url1 = base_url + 'profit-lossVI/'+ MC_ticker +'/#' + MC_ticker
        standalone_url2 = base_url + 'profit-lossVI/'+ MC_ticker +'/2#' + MC_ticker
        standalone_url3 = base_url + 'profit-lossVI/'+ MC_ticker +'/3#' + MC_ticker
        standalone_url4 = base_url + 'profit-lossVI/'+ MC_ticker +'/4#' + MC_ticker
        consolidated_url1 = base_url + 'consolidated-profit-lossVI/'+ MC_ticker +'/#' + MC_ticker
        consolidated_url2 = base_url + 'consolidated-profit-lossVI/'+ MC_ticker +'/2#' + MC_ticker
        consolidated_url3 = base_url + 'consolidated-profit-lossVI/'+ MC_ticker +'/3#' + MC_ticker
        consolidated_url4 = base_url + 'consolidated-profit-lossVI/'+ MC_ticker +'/4#' + MC_ticker
    elif financial_type == "cash flow":
        standalone_url1 = base_url + 'cash-flowVI/'+ MC_ticker +'/#' + MC_ticker
        standalone_url2 = base_url + 'cash-flowVI/'+ MC_ticker +'/2#' + MC_ticker
        standalone_url3 = base_url + 'cash-flowVI/'+ MC_ticker +'/3#' + MC_ticker
        standalone_url4 = base_url + 'cash-flowVI/'+ MC_ticker +'/4#' + MC_ticker
        consolidated_url1 = base_url + 'consolidated-cash-flowVI/'+ MC_ticker +'/#' + MC_ticker
        consolidated_url2 = base_url + 'consolidated-cash-flowVI/'+ MC_ticker +'/2#' + MC_ticker
        consolidated_url3 = base_url + 'consolidated-cash-flowVI/'+ MC_ticker +'/3#' + MC_ticker
        consolidated_url4 = base_url + 'consolidated-cash-flowVI/'+ MC_ticker +'/4#' + MC_ticker
    elif financial_type == "ratios":
        standalone_url1 = base_url + 'ratiosVI/'+ MC_ticker +'/#' + MC_ticker
        standalone_url2 = base_url + 'ratiosVI/'+ MC_ticker +'/2#' + MC_ticker
        standalone_url3 = base_url + 'ratiosVI/'+ MC_ticker +'/3#' + MC_ticker
        standalone_url4 = base_url + 'ratiosVI/'+ MC_ticker +'/4#' + MC_ticker
        consolidated_url1 = base_url + 'consolidated-ratiosVI/'+ MC_ticker +'/#' + MC_ticker
        consolidated_url2 = base_url + 'consolidated-ratiosVI/'+ MC_ticker +'/2#' + MC_ticker
        consolidated_url3 = base_url + 'consolidated-ratiosVI/'+ MC_ticker +'/3#' + MC_ticker
        consolidated_url4 = base_url + 'consolidated-ratiosVI/'+ MC_ticker +'/4#' + MC_ticker
    return({"standalone":[standalone_url1, standalone_url2, standalone_url3, standalone_url4],"consolidated":[consolidated_url1, consolidated_url2, consolidated_url3, consolidated_url4]})

def google_moneycontrol_base_sitename(stock_ticker):
    """
    This function will search the base name for the moneycontrol site of the stock_ticker. 
    Final Output will be the base URL + Moneycontrol ticker symbol 
    """
    from googlesearch import search
    import re
    query_string = "moneycontrol fianacials of " + stock_ticker
    ratio_url = ""
    google_search_op_string = search(query = query_string, stop =20 )
    for url in google_search_op_string:
        #print(url)
        match = re.match("(https://www.moneycontrol.com/financials/.*?/).*?[/]([0-9A-Za-z]+)", url)
        #https://www.moneycontrol.com/financials/relianceindustries/balance-sheetVI/ri
        if match:
            ratio_url = match.group(1)
            MC_ticker = match.group(2)
            break
    return [ratio_url, MC_ticker]

def pull_attributes_from_moneycontrol(stock_ticker, url):
    """
    Pull data from moneycontrol based on the URL given. Pull the main attribute with values. 
    Differentiate the main name , year & other values.
    Final output will be as a dictionary.
    """
    import requests, re, json
    from bs4 import BeautifulSoup
    #print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    td_all  = soup.find_all('td')
    year = []
    key_item_pair = {}
    for td in td_all:
        if re.match(".*href=.*", str(td)) is None and re.match(".*td class=.*", str(td)) is None and re.match(".td....td.", str(td)) is None and re.match(".td.12 mths..td.", str(td)) is None:
            match = re.match(".td.(.*)[<]span class=.ttn.[>](.*)[<].*[>][<].*[>]", str(td))
            if match:
                main_key = match.group(1) + match.group(2)
                name_match = re.match("(.*)amp;(.*)", main_key)
                if name_match:
                    main_key = name_match.group(1) + name_match.group(2)
                #print(main_key)
            else:
                match = re.match(".td.Mar ([0-9][0-9])..td.", str(td))
                if match:
                    current_year = "20" + match.group(1)
                    year.append(current_year)
                else:
                    match = re.match(".td.([a-zA-Z].*)..td.", str(td))
                    if match:
                        key = match.group(1)
                        key_item_pair[key]=[]
                    else:
                        match = re.match(".td.([-,.0-9]+)..td.",str(td))
                        if match:
                            item = match.group(1)
                            key_item_pair[key].append(item)
    init = {"Name": main_key, "Year": year}
    financials = {**init, **key_item_pair}
    return financials

def build_dataframe_and_print_to_excel(financial_data, stock_ticker):
    """
    This function will build the pandas dataframe & make the excel file.
    """
    import pandas as pd
    import re
    filepath = '/home/arnashree/analyzeninvest-projects/NSE_Financial_Database/excel_path/'
    xlsx_path = filepath + stock_ticker + '.xlsx'
    writer = pd.ExcelWriter(xlsx_path, engine='openpyxl')
    for key in financial_data:
        print(key)
        df_item = pd.DataFrame(data=financial_data[key])
        item = financial_data[key]
        standalone_item = item["Standalone"]
        consolidated_item = item["Consolidated"]
        for sub_key in standalone_item:
            length = len(standalone_item[sub_key])
            if length == 0 or length < 20:
                filler = ["--"] * (20 - length)
                standalone_item[sub_key].extend(filler)
        for sub_key in consolidated_item:
            length = len(consolidated_item[sub_key])
            if length == 0 or length < 20:
                filler = ["--"] * (20 - length)
                consolidated_item[sub_key].extend(filler)
        df_standalone_item = pd.DataFrame(data = standalone_item, index = standalone_item["Year"])
        df_consolidated_item = pd.DataFrame(data = consolidated_item, index = consolidated_item["Year"])
        df_standalone_item = df_standalone_item.drop(columns=["Name", "Year"])
        df_consolidated_item = df_consolidated_item.drop(columns=["Name", "Year"])
        df_standalone_item.index.name = "Year"
        df_consolidated_item.index.name = "Year"
        #print(standalone_item["Name"])
        if re.match("Balance Sheet", standalone_item["Name"]):
            sheet_name = "Balance_Sheet"
            #print(sheet_name)
        elif re.match("Profit & Loss", standalone_item["Name"]):
            sheet_name = "Profit_and_Loss"
            #print(sheet_name)
        elif re.match("Key Financial Ratios", standalone_item["Name"]):
            sheet_name = "Ratio"
            #print(sheet_name)
        elif re.match("Cash Flow", standalone_item["Name"]):
            sheet_name = "Cash_Flow"
            #print(sheet_name)
        standalone_sheet_name = "Standalone_" + sheet_name
        consolidated_sheet_name = "Consolidated_" + sheet_name
        df_standalone_item.to_excel(writer, sheet_name = standalone_sheet_name, float_format="%.2f", index=True, startrow=1)
        writer.save()
        df_consolidated_item.to_excel(writer, sheet_name = consolidated_sheet_name, float_format="%.2f", index=True, startrow=1)
        writer.save()
    writer.save()
    writer.close()

    

def main():
    """
    This is only for testing as of now.
    """
    #cash_flow = pull_cash_flow_statement_from_moenyontrol('TCS')
    #print(cash_flow)
    #print(get_url_of_moneycontrol_from_ticker('TCS', "cash flow"))
    #print(google_moneycontrol_base_sitename('TCS'))
    import time
    t0 = time.time()
    stock_ticker = 'RIL'
    stock_financials = pull_financial_statement_from_moneycontrol(stock_ticker)
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

