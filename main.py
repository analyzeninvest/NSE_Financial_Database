#!/usr/bin/env python

def pull_financial_statement_from_moneycontrol(stock_ticker):
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
    all_urls = get_url_of_moneycontrol_from_ticker(stock_ticker, "income statement")
    standalone_profit_and_loss_statement_current_page = []
    consolidated_profit_and_loss_statement_current_page = []
    for url in all_urls["standalone"]:
        standalone_profit_and_loss_statement_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    for url in all_urls["consolidated"]:
        consolidated_profit_and_loss_statement_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    profit_and_loss_statements = {"Standalone" : standalone_profit_and_loss_statement_current_page, "consolidated" : consolidated_profit_and_loss_statement_current_page}
    return(profit_and_loss_statements)

def pull_balance_sheet_from_moenycontrol(stock_ticker):
    all_urls = get_url_of_moneycontrol_from_ticker(stock_ticker, "balance sheet")
    standalone_balance_sheet_current_page = []
    consolidated_balance_sheet_current_page = []
    for url in all_urls["standalone"]:
        standalone_balance_sheet_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    for url in all_urls["consolidated"]:
        consolidated_balance_sheet_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    balance_sheets = {"Standalone" : standalone_balance_sheet_current_page, "consolidated" : consolidated_balance_sheet_current_page}
    return(balance_sheets)

def pull_cash_flow_statement_from_moenyontrol(stock_ticker):
    all_urls = get_url_of_moneycontrol_from_ticker(stock_ticker, "cash flow")
    standalone_cash_flow_statement_current_page = []
    consolidated_cash_flow_statement_current_page = []
    for url in all_urls["standalone"]:
        standalone_cash_flow_statement_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    for url in all_urls["consolidated"]:
        consolidated_cash_flow_statement_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    cash_flow_statements = {"Standalone" : standalone_cash_flow_statement_current_page, "consolidated" : consolidated_cash_flow_statement_current_page}
    return(cash_flow_statements)

def pull_key_ratios_from_moneycontrol(stock_ticker):
    all_urls = get_url_of_moneycontrol_from_ticker(stock_ticker, "ratios")
    standalone_ratios_current_page = []
    consolidated_ratios_current_page = []
    for url in all_urls["standalone"]:
        standalone_ratios_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    for url in all_urls["consolidated"]:
        consolidated_ratios_current_page.append(pull_attributes_from_moneycontrol(stock_ticker, url))
    ratios = {"Standalone" : standalone_ratios_current_page, "consolidated" : consolidated_ratios_current_page}
    return(ratios)

def get_url_of_moneycontrol_from_ticker(stock_ticker, financial_type):
    """
    This function will get the URL for the stock of moneycontrol website.
    example: 
    TCS Standalone Balance Sheet FY 20 - 16: https://www.moneycontrol.com/financials/tataconsultancyservices/balance-sheetVI/TCS#TCS
    TCS Standalone Balance Sheet FY 15 - 11: https://www.moneycontrol.com/financials/tataconsultancyservices/balance-sheetVI/TCS/2#TCS
    TCS Standalone Balance Sheet FY 10 - 06: https://www.moneycontrol.com/financials/tataconsultancyservices/balance-sheetVI/TCS/3#TCS
    TCS Standalone Balance Sheet FY 05 - 04: https://www.moneycontrol.com/financials/tataconsultancyservices/balance-sheetVI/TCS/4#TCS
    TCS Consolidated Balance Sheet FY 20 - 16: https://www.moneycontrol.com/financials/tataconsultancyservices/consolidated-balance-sheetVI/TCS#TCS
    TCS Consolidated Balance Sheet FY 15 - 11: https://www.moneycontrol.com/financials/tataconsultancyservices/consolidated-balance-sheetVI/TCS/2#TCS
    TCS Consolidated Balance Sheet FY 10 - 06: https://www.moneycontrol.com/financials/tataconsultancyservices/consolidated-balance-sheetVI/TCS/3#TCS
    TCS Consolidated Balance Sheet FY 05 - 04: https://www.moneycontrol.com/financials/tataconsultancyservices/consolidated-balance-sheetVI/TCS/4#TCS
    TCS Standalone Profit & Loss FY 20 - 16: https://www.moneycontrol.com/financials/tataconsultancyservices/profit-lossVI/TCS#TCS
    TCS Consolidated Profit & Loss FY 20 - 16: https://www.moneycontrol.com/financials/tataconsultancyservices/consolidated-profit-lossVI/TCS#TCS
    TCS Standalone Cash Flow FY 20 - 16: https://www.moneycontrol.com/financials/tataconsultancyservices/cash-flowVI/TCS#TCS
    TCS Consolidated Cash Flow FY 20 - 16: https://www.moneycontrol.com/financials/tataconsultancyservices/consolidated-cash-flowVI/TCS#TCS
    TCS Standalone Key Ratio FY 20 - 16: https://www.moneycontrol.com/financials/tataconsultancyservices/ratiosVI/TCS#TCS
    TCS Consolidated Key Ratio FY 20 - 16: https://www.moneycontrol.com/financials/tataconsultancyservices/consolidated-ratiosVI/TCS#TCS
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
    """
    from googlesearch import search
    import re
    query_string = "moneycontrol fianacials of " + stock_ticker
    ratio_url = ""
    google_search_op_string = search(query = query_string, stop =20 )
    for url in google_search_op_string:
        #print(url)
        match = re.match("(https://www.moneycontrol.com/financials/.*?/).*?[/]([0-9A-Z]+)", url)
        if match:
            ratio_url = match.group(1)
            MC_ticker = match.group(2)
            break
    return [ratio_url, MC_ticker]


def pull_attributes_from_moneycontrol(stock_ticker, url):
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

def main():
    #cash_flow = pull_cash_flow_statement_from_moenyontrol('TCS')
    #print(cash_flow)
    #print(get_url_of_moneycontrol_from_ticker('TCS', "cash flow"))
    #print(google_moneycontrol_base_sitename('TCS'))
    print(pull_financial_statement_from_moneycontrol('TCS'))
main()

"""
target output:
TCS.json
{
"Stock Name" : "Tata Consultancy Services"
"Ticker" : "TCS"
"Fianacial Annual" {
"Standalone"{
"Profot & Loss Statement"{
"year" : ["2020", "2019", "2018", "2017", "2016"],
"Revenue from operations[gross]" : [131306.00, 123170.00, 97356.00, 92693.00, 85864.00]

},
"Balance Sheet"{
},
"Cash Flow Statement"{
},
"Ratios"{
}
},
"Consolidated"{
"Profot & Loss Statement"{
},
"Balance Sheet"{
},
"Cash Flow Statement"{
},
"Ratios"{
}
}
}

}

"""
