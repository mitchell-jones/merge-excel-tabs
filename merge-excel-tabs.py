import pandas as pd
import sys
import xlrd

xls = pd.ExcelFile(str(sys.argv[1]))

def load_df(name):
    df2 = pd.read_excel(xls, name)
    df2['SheetName'] = name
    return df2

def concat(second_df):
    global df_master
    df_master = pd.concat([df_master, second_df], axis=0)

def main():
    sheetnames = xls.sheet_names
    global df_master
    df_master = load_df(sheetnames.pop(0))
    df_master.head()

    for sheet in sheetnames:
        df_temp = load_df(sheet)
        concat(df_temp)

    filename = sys.argv[2]
    df_master.to_csv(filename, sep = '|', quotechar = '"', encoding='utf-8')

if __name__ == "__main__":
    main()