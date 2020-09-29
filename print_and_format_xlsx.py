#!/usr/bin/env python

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
        #print(key)
        df_item = pd.DataFrame(data=financial_data[key])
        item = financial_data[key]
        standalone_item = item["Standalone"]
        consolidated_item = item["Consolidated"]
        for sub_key in standalone_item:
            length = len(standalone_item[sub_key])
            #print(length)
            if length == 0 and type(standalone_item[sub_key]) != str :
                standalone_item[sub_key] = ["--"] * 20
            elif length < 20 and type(standalone_item[sub_key]) != str :
                filler = ["--"] * (20 - length)
                #print(sub_key)
                standalone_item[sub_key].extend(filler)
        for sub_key in consolidated_item:
            length = len(consolidated_item[sub_key])
            #print(length)
            if length == 0 and type(consolidated_item[sub_key]) != str :
                consolidated_item[sub_key] = ["--"] * 20
            elif length < 20 and type(consolidated_item[sub_key]) != str :
                filler = ["--"] * (20 - length)
                consolidated_item[sub_key].extend(filler)
        df_standalone_item = pd.DataFrame(data = standalone_item, index = standalone_item["Year"])
        df_consolidated_item = pd.DataFrame(data = consolidated_item, index = consolidated_item["Year"])
        df_standalone_item = df_standalone_item.drop(columns=["Name", "Year"])
        df_consolidated_item = df_consolidated_item.drop(columns=["Name", "Year"])
        df_standalone_item.index.name = "Year"
        df_consolidated_item.index.name = "Year"
        #print(standalone_item["Name"])
        sheet_name = ""
        if re.match("Balance Sheet", standalone_item["Name"]) or re.match("Balance Sheet", consolidated_item["Name"]):
            sheet_name = "Balance_Sheet"
            #print(sheet_name)
        elif re.match("Profit & Loss", standalone_item["Name"]) or re.match("Profit & Loss", consolidated_item["Name"]):
            sheet_name = "Profit_and_Loss"
            #print(sheet_name)
        elif re.match("Key Financial Ratios", standalone_item["Name"]) or re.match("Key Financial Ratios", consolidated_item["Name"]):
            sheet_name = "Ratio"
            #print(sheet_name)
        elif re.match("Cash Flow", standalone_item["Name"]) or re.match("Cash Flow", consolidated_item["Name"]):
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
