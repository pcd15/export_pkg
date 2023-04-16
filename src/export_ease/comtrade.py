import comtradeapicall
import datetime
import pandas
import os

class Comtrade:

    cwd = os.getcwd()
    parent = os.path.dirname(cwd)
    directory = os.path.join(parent, "data")
    subscription_key = "9be8b0a6438a4940bd592c691bb2c4ca"

    def __init__(self):
        pass

    # function to get all available country-pair export data
    @classmethod
    def get_all_exports(cls, freq, year):
        if freq == "B":
            Comtrade.get_all_exports("A", year)
            Comtrade.get_all_exports("M", year)
        else:
            date = year
            if freq == 'M':
                date = f'{year}01,{year}02,{year}03,{year}04,{year}05,{year}06,{year}07,{year}08,{year}09,{year}10,{year}11,{year}12'
            mydf = comtradeapicall.getFinalData(Comtrade.subscription_key, typeCode='C', freqCode=freq, clCode='HS', period=date,
                                                reporterCode=None, cmdCode='TOTAL', flowCode='X', partnerCode=None,
                                                partner2Code=None,
                                                customsCode=None, motCode=None, maxRecords=None, format_output='JSON',
                                                aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)
            df = pandas.DataFrame(mydf)
            file_name = f'comtrade_all_exports_{year}{freq}.csv'
            print(f'Writing {file_name}....')
            df.to_csv(os.path.join(Comtrade.directory, file_name))

    # function to get all available total-export data (i.e., partner is world)
    @classmethod
    def get_total_exports(cls, freq, year):
        if freq == "B":
            Comtrade.get_total_exports("A", year)
            Comtrade.get_total_exports("M", year)
        else:
            date = year
            if freq == 'M':
                date = f'{year}01,{year}02,{year}03,{year}04,{year}05,{year}06,{year}07,{year}08,{year}09,{year}10,{year}11,{year}12'
            mydf = comtradeapicall.getFinalData(Comtrade.subscription_key, typeCode='C', freqCode=freq, clCode='HS', period=date,
                                                reporterCode=None, cmdCode='TOTAL', flowCode='X', partnerCode=0,
                                                partner2Code=None,
                                                customsCode=None, motCode=None, maxRecords=None, format_output='JSON',
                                                aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)
            df = pandas.DataFrame(mydf)
            file_name = f'comtrade_total_exports_{year}{freq}.csv'
            print(f'Writing {file_name}....')
            df.to_csv(os.path.join(Comtrade.directory, file_name))