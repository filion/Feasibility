import sys
import datetime
import classes as cl
# import requests
import pandas as pd
import numpy as np
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import msvcrt as m



def wait():
    m.getch()


def create_entities(reg):

    thermal_entities_df = reg[reg.loc[:, 'Type'] == 'THERMAL']
    hydro_entities_df = reg[reg.loc[:, 'Type'] == 'HYDRO']

    thermal_entities_dictionary = {}
    hydro_entities_dictionary = {}

    for i, v in thermal_entities_df.iterrows():
        entity = cl.BaseEntity(v['ENTITY'], v['Type'])
        thermal_entities_dictionary[v['ENTITY']] = entity

    for i, v in hydro_entities_df.iterrows():
        entity = cl.BaseEntity(v['ENTITY'], v['Type'])
        hydro_entities_dictionary[v['ENTITY']] = entity

    return thermal_entities_dictionary, hydro_entities_dictionary


def get_utc_timeseries(date):
    if not isinstance(date, int):
        raise TypeError(
            'Argument %r must be of type %s in a YYYYDDMM format.' % (date, int)
        )
    start = datetime.datetime.strptime(str(date), '%Y%m%d')
    end = start + datetime.timedelta(days=1)
    timeseries_cet = pd.date_range(start=start, end=end, freq='30T', tz='cet', inclusive='left')
    timeseries_utc = timeseries_cet.tz_convert('utc')
    return timeseries_utc

#
# downloadlink = "https://www.admie.gr/sites/default/files/attached-files/type-file/2022/10/20221005"
# def read_isp_requirements:
#     raw_data = pd.read_excel(req_path, engine='openpyxl', index_col=0, header=None)
#     RES_df = raw_data.loc['RES Forecast':'Non-Dispatchable Load Forecast'].drop(
#         'Non-Dispatchable Load Forecast')
#     RES_df = RES_df.T.set_index('RES Forecast').T
#     RES_df.index.name=None
#
#     RES_df.drop(labels=np.nan, axis=1, inplace=True)
#
# def read_henex_results:
# def read_availabilities
# def isp_requirements(req_path):
#     data = dict()
#     # Read data and create timeseries for column names.
#     # print(raw_data)
#
#     RES_df = raw_data.loc['RES Forecast':'Non-Dispatchable Load Forecast'].drop(
#         'Non-Dispatchable Load Forecast')
#     RES_df = RES_df.T.set_index('RES Forecast').T
#     RES_df.index.name=None
#     RES_df.drop(labels=np.nan, axis=1, inplace=True)
#     print(RES_df)
#
#     Load_df = raw_data.loc['Non-Dispatchable Load Forecast':'Mandatory Hydro'].drop(
#         'Mandatory Hydro')
#     Load_df = Load_df.T.set_index('Non-Dispatchable Load Forecast').T
#     Load_df.index.name=None
#     Load_df.drop(labels=np.nan, axis=1, inplace=True)
#     print(Load_df)
#
#     Mandatory_Hydro_df = raw_data.loc['Mandatory Hydro':'Commissioning'].drop(
#         'Commissioning')
#     print(Mandatory_Hydro_df)
#     Mandatory_Hydro_df.columns = Mandatory_Hydro_df.iloc[0]
#     Mandatory_Hydro_df.drop(index=Mandatory_Hydro_df.index[0], axis=0, inplace=True)
#     Mandatory_Hydro_df.rename(columns={np.nan: 'Entity'}, inplace=True)
#     Mandatory_Hydro_df.set_index('Entity', inplace=True)
#     Mandatory_Hydro_df.rename(index={np.nan: 'Total'}, inplace=True)
#     # Mandatory_Hydro_df.columns = Mandatory_Hydro_df.iloc[0]
#     # Mandatory_Hydro_df=Mandatory_Hydro_df.T.set_index('Mandatory Hydro').T
#     # Mandatory_Hydro_df.rename(columns={'np.nan':'Entity'}, inplace = True)
#     print(Mandatory_Hydro_df)
#
#     Commissioning_df = raw_data.loc['Commissioning':'Reserve Requirements'].drop(
#         'Reserve Requirements')
#     print(Commissioning_df)
#
#     Reserves_df = raw_data.loc['Reserve Requirements':]
#     print(Reserves_df)
#
#
# path = r'C:\Users\t.daglis\PycharmProjects\ISP\20220328_ISP1Requirements_02.xlsx'
# isp_requirements(path)
# # raw_data = pd.read_excel(path, engine='openpyxl', index_col = [0, 1], header=None)
# # print(raw_data)
