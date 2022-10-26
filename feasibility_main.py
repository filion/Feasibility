if __name__== "__main__":
    import input_functions as fn
    import sys
    import datetime
    # import requests
    import pandas as pd
    import numpy as np

    # from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
    try:
        registry = pd.read_excel(r'./registry.xlsx', sheet_name=None)
        ccgt_df = registry['CCGT']
        entities_df = registry['Entities']
    except FileNotFoundError:
        print("Error: Registry file not found. Press any key to continue...")
        fn.wait()
        sys.exit(1)
    except KeyError as err:
        print("Error: Registry file is missing " + str(err) + f' entries.\nPress any key to exit...')
        fn.wait()
        sys.exit(1)
    thermal_entities, hydro_entities = fn.create_entities(entities_df)

    delivery_date = datetime.date.today()
    year = delivery_date.year
    month = delivery_date.month
    day = delivery_date.day
    downloadlink = f"https://www.admie.gr/sites/default/files/attached-files/type-file/" + str(year) + "/" + str(
        month) + "/" + delivery_date.strftime('%Y%m%d') + '_ISP1Requirements_01.xlsx'

    df = pd.read_excel(downloadlink, engine='openpyxl', index_col=None, header=None)
    df.drop(0, inplace=True)

    groups = df.groupby((df.iloc[:, 0] == 'Total System').shift(fill_value=False).cumsum())
    req_dict = {}
    for i, sub_df in groups:
        sub_df.columns=sub_df.iloc[0]
        sub_df.drop(sub_df.index[0], axis=0, inplace=True)
        sub_df.reset_index(drop=True, inplace=True)
        sub_df.columns.name=sub_df.columns[0]
        sub_df.rename(columns={sub_df.columns[0]: 'Type', sub_df.columns[1]: 'Entity'}, inplace=True)
        sub_df.set_index(['Type', 'Entity'], inplace=True)
        utc_timeseries = fn.get_utc_timeseries(int(delivery_date.strftime('%Y%m%d')))
        old_timeseries=sub_df.loc[:,'00:00':'23:30'].columns
        timeseries_dict=dict(zip(old_timeseries, utc_timeseries))
        sub_df.rename(columns=timeseries_dict, inplace=True)
        # print(sub_df)
        req_dict[sub_df.columns.name]=sub_df


    for entity in req_dict['Mandatory Hydro'].iterrows():
        # TODO Write properly the entity
        name = entity[0][1]
        print(entity[1])
        if name in hydro_entities.keys():
            hydro_entities[name].market_schedule = entity[1].loc[timeseries_dict]
    # print(req_dict['Mandatory Hydro'].loc[:, utc_timeseries])

# for i,v in req_dict.items():
    # print(i)
        # print(sub_df.T.set_index(0).T)
        # sub_df.set_index([0,1], inplace=True)
        # sub_df.T.set_index(1, inplace=True)
        # print(sub_df)

        # sub_df.set_index('1', inplace=True)
        # print(sub_df)
    #
    # utc_timeseries = fn.get_utc_timeseries(int(delivery_date.strftime('%Y%m%d')))
    # old_timeseries=df.loc[:,'00:00':'23:30'].columns
    # timeseries_dict=dict(zip(old_timeseries, utc_timeseries))
    # df.rename(columns=timeseries_dict, inplace=True)

    #
