#!/usr/bin/env python

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
                    merged_dict[key1] = dict1.get(key1)
    return(merged_dict)

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
        current_financials = pull_attributes_from_moneycontrol(stock_ticker, url)
        if current_financials["Name"] != "--":
            standalone_profit_and_loss_statement_current_page.append(current_financials)
    for url in all_urls["consolidated"]:
        current_financials = pull_attributes_from_moneycontrol(stock_ticker, url)
        if current_financials["Name"] != "--":
            consolidated_profit_and_loss_statement_current_page.append(current_financials)
    standalone_array_length = len(standalone_profit_and_loss_statement_current_page)
    if standalone_array_length == 4:
        standalone_profit_and_loss_statement = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                merge_array_of_2_dictionary_with_same_key(
                    standalone_profit_and_loss_statement_current_page[0],
                    standalone_profit_and_loss_statement_current_page[1]),
                standalone_profit_and_loss_statement_current_page[2]),
            standalone_profit_and_loss_statement_current_page[3])
    elif standalone_array_length == 3:
        standalone_profit_and_loss_statement = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                standalone_profit_and_loss_statement_current_page[0],
                standalone_profit_and_loss_statement_current_page[1]),
            standalone_profit_and_loss_statement_current_page[2])
    elif standalone_array_length == 2:
        standalone_profit_and_loss_statement = merge_array_of_2_dictionary_with_same_key(
            standalone_profit_and_loss_statement_current_page[0],
            standalone_profit_and_loss_statement_current_page[1])
    elif standalone_array_length == 1:
        standalone_profit_and_loss_statement = standalone_profit_and_loss_statement_current_page[0]
    elif standalone_array_length == 0:
        standalone_profit_and_loss_statement = {"Name":"--", "Year":[]}
    consolidated_array_length = len(consolidated_profit_and_loss_statement_current_page)
    if consolidated_array_length == 4:
        consolidated_profit_and_loss_statement = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                merge_array_of_2_dictionary_with_same_key(
                    consolidated_profit_and_loss_statement_current_page[0],
                    consolidated_profit_and_loss_statement_current_page[1]),
                consolidated_profit_and_loss_statement_current_page[2]),
            consolidated_profit_and_loss_statement_current_page[3])
    elif consolidated_array_length == 3:
        consolidated_profit_and_loss_statement = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                consolidated_profit_and_loss_statement_current_page[0],
                consolidated_profit_and_loss_statement_current_page[1]),
            consolidated_profit_and_loss_statement_current_page[2])
    elif consolidated_array_length == 2:
        consolidated_profit_and_loss_statement = merge_array_of_2_dictionary_with_same_key(
            consolidated_profit_and_loss_statement_current_page[0],
            consolidated_profit_and_loss_statement_current_page[1])
    elif consolidated_array_length == 1:
        consolidated_profit_and_loss_statement = consolidated_profit_and_loss_statement_current_page[0]
    elif consolidated_array_length == 0:
        consolidated_profit_and_loss_statement = {"Name":"--", "Year":[]}
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
        current_financials = pull_attributes_from_moneycontrol(stock_ticker, url)
        if current_financials["Name"] != "--":
            standalone_balance_sheet_current_page.append(current_financials)
    for url in all_urls["consolidated"]:
        current_financials = pull_attributes_from_moneycontrol(stock_ticker, url)
        if current_financials["Name"] != "--":
            consolidated_balance_sheet_current_page.append(current_financials)
    standalone_array_length = len(standalone_balance_sheet_current_page)
    if standalone_array_length == 4:
        standalone_balance_sheet = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                merge_array_of_2_dictionary_with_same_key(
                    standalone_balance_sheet_current_page[0],
                    standalone_balance_sheet_current_page[1]),
                standalone_balance_sheet_current_page[2]),
            standalone_balance_sheet_current_page[3])
    elif standalone_array_length == 3:
        standalone_balance_sheet = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                standalone_balance_sheet_current_page[0],
                standalone_balance_sheet_current_page[1]),
            standalone_balance_sheet_current_page[2])
    elif standalone_array_length == 2:
        standalone_balance_sheet = merge_array_of_2_dictionary_with_same_key(
            standalone_balance_sheet_current_page[0],
            standalone_balance_sheet_current_page[1])
    elif standalone_array_length == 1:
        standalone_balance_sheet = standalone_balance_sheet_current_page[0]
    elif standalone_array_length == 0:
        standalone_balance_sheet = {"Name":"--", "Year":[]}
    consolidated_array_length = len(consolidated_balance_sheet_current_page)
    if consolidated_array_length == 4:
        consolidated_balance_sheet = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                merge_array_of_2_dictionary_with_same_key(
                    consolidated_balance_sheet_current_page[0],
                    consolidated_balance_sheet_current_page[1]),
                consolidated_balance_sheet_current_page[2]),
            consolidated_balance_sheet_current_page[3])
    elif consolidated_array_length == 3:
        consolidated_balance_sheet = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                consolidated_balance_sheet_current_page[0],
                consolidated_balance_sheet_current_page[1]),
            consolidated_balance_sheet_current_page[2])
    elif consolidated_array_length == 2:
        consolidated_balance_sheet = merge_array_of_2_dictionary_with_same_key(
            consolidated_balance_sheet_current_page[0],
            consolidated_balance_sheet_current_page[1])
    elif consolidated_array_length == 1:
        consolidated_balance_sheet = consolidated_balance_sheet_current_page[0]
    elif consolidated_array_length == 0:
        consolidated_balance_sheet = {"Name":"--", "Year":[]}
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
        current_financials = pull_attributes_from_moneycontrol(stock_ticker, url)
        if current_financials["Name"] != "--":
            standalone_cash_flow_statement_current_page.append(current_financials)
    for url in all_urls["consolidated"]:
        current_financials = pull_attributes_from_moneycontrol(stock_ticker, url)
        if current_financials["Name"] != "--":
            consolidated_cash_flow_statement_current_page.append(current_financials)
    standalone_array_length = len(standalone_cash_flow_statement_current_page)
    if standalone_array_length == 4:
        standalone_cash_flow_statement = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                merge_array_of_2_dictionary_with_same_key(
                    standalone_cash_flow_statement_current_page[0],
                    standalone_cash_flow_statement_current_page[1]),
                standalone_cash_flow_statement_current_page[2]),
            standalone_cash_flow_statement_current_page[3])
    elif standalone_array_length == 3:
        standalone_cash_flow_statement = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                standalone_cash_flow_statement_current_page[0],
                standalone_cash_flow_statement_current_page[1]),
            standalone_cash_flow_statement_current_page[2])
    elif standalone_array_length == 2:
        standalone_cash_flow_statement = merge_array_of_2_dictionary_with_same_key(
            standalone_cash_flow_statement_current_page[0],
            standalone_cash_flow_statement_current_page[1])
    elif standalone_array_length == 1:
        standalone_cash_flow_statement = standalone_cash_flow_statement_current_page[0]
    elif standalone_array_length == 0:
        standalone_cash_flow_statement = {"Name":"--", "Year":[]}
    consolidated_array_length = len(consolidated_cash_flow_statement_current_page)
    if consolidated_array_length == 4:
        consolidated_cash_flow_statement = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                merge_array_of_2_dictionary_with_same_key(
                    consolidated_cash_flow_statement_current_page[0],
                    consolidated_cash_flow_statement_current_page[1]),
                consolidated_cash_flow_statement_current_page[2]),
            consolidated_cash_flow_statement_current_page[3])
    elif consolidated_array_length == 3:
        consolidated_cash_flow_statement = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                consolidated_cash_flow_statement_current_page[0],
                consolidated_cash_flow_statement_current_page[1]),
            consolidated_cash_flow_statement_current_page[2])
    elif consolidated_array_length == 2:
        consolidated_cash_flow_statement = merge_array_of_2_dictionary_with_same_key(
                consolidated_cash_flow_statement_current_page[0],
                consolidated_cash_flow_statement_current_page[1])
    elif consolidated_array_length == 1:
        consolidated_cash_flow_statement = consolidated_cash_flow_statement_current_page[0]
    elif consolidated_array_length == 0:
        consolidated_cash_flow_statement = {"Name":"--", "Year":[]}
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
        current_financials = pull_attributes_from_moneycontrol(stock_ticker, url)
        if current_financials["Name"] != "--":
            standalone_ratios_current_page.append(current_financials)
    for url in all_urls["consolidated"]:
        current_financials = pull_attributes_from_moneycontrol(stock_ticker, url)
        if current_financials["Name"] != "--":
            consolidated_ratios_current_page.append(current_financials)
    standalone_array_length = len(standalone_ratios_current_page)
    if standalone_array_length == 4:
        standalone_ratios = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                merge_array_of_2_dictionary_with_same_key(
                    standalone_ratios_current_page[0],
                    standalone_ratios_current_page[1]),
                standalone_ratios_current_page[2]),
            standalone_ratios_current_page[3])
    elif standalone_array_length == 3:
        standalone_ratios = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                standalone_ratios_current_page[0],
                standalone_ratios_current_page[1]),
            standalone_ratios_current_page[2])
    elif standalone_array_length == 2:
        standalone_ratios = merge_array_of_2_dictionary_with_same_key(
            standalone_ratios_current_page[0],
            standalone_ratios_current_page[1])
    elif standalone_array_length == 1:
        standalone_ratios = standalone_ratios_current_page[0]
    elif standalone_array_length == 0:
        standalone_ratios = {"Name":"--", "Year":[]}
    consolidated_array_length = len(consolidated_ratios_current_page)
    if consolidated_array_length == 4:
        consolidated_ratios = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                merge_array_of_2_dictionary_with_same_key(
                    consolidated_ratios_current_page[0],
                    consolidated_ratios_current_page[1]),
                consolidated_ratios_current_page[2]),
            consolidated_ratios_current_page[3])
    elif consolidated_array_length == 3:
        consolidated_ratios = merge_array_of_2_dictionary_with_same_key(
            merge_array_of_2_dictionary_with_same_key(
                consolidated_ratios_current_page[0],
                consolidated_ratios_current_page[1]),
            consolidated_ratios_current_page[2])
    elif consolidated_array_length == 2:
        consolidated_ratios = merge_array_of_2_dictionary_with_same_key(
            consolidated_ratios_current_page[0],
            consolidated_ratios_current_page[1])
    elif consolidated_array_length == 1:
        consolidated_ratios = consolidated_ratios_current_page[0]
    elif consolidated_array_length == 0:
        consolidated_ratios = {"Name":"--", "Year":[]}
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
    #print({"standalone":[standalone_url1, standalone_url2, standalone_url3, standalone_url4],"consolidated":[consolidated_url1, consolidated_url2, consolidated_url3, consolidated_url4]})
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
        match = re.match("(https://www.moneycontrol.com/financials/[a-zA-Z0-9-_]+/).*[/]([0-9A-Za-z]+)", url)
        #Quarterly_match = re.match(".*quarterly-results", url)
        #https://www.moneycontrol.com/financials/relianceindustries/balance-sheetVI/ri
        #>>> https://www.moneycontrol.com/financials/astramicrowaveproducts/results/quarterly-results/amp01
        if match :
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
    main_key = "--"
    year = []
    key_item_pair = {}
    for td in td_all:
        if re.match(".*href=.*", str(td)) is None and \
        re.match(".*td class=.*", str(td)) is None and \
        re.match(".td....td.", str(td)) is None and \
        re.match(".td.12 mths..td.", str(td)) is None:
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
    #print(key_item_pair)
    init = {"Name": main_key, "Year": year}
    financials = {**init, **key_item_pair}
    #print(financials)
    return financials

