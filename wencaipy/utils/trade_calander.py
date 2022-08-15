import os
import datetime
from pprint import pprint
import requests
import pandas as pd
import numpy as np
import pickle
from wencaipy.common.dataToExcel import data_to_excel, read_data_from_excel

rest_days_df = None
chinese_holidays_range = None


def today():
    return datetime.date.today()


def date2str(cursor_date):
    """
    explanation:
        对输入日期进行格式化处理，返回格式为 "%Y-%m-%d" 格式字符串
        支持格式包括:
        1. str: "%Y%m%d" "%Y%m%d%H%M%S", "%Y%m%d %H:%M:%S",
                "%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H%M%S"
        2. datetime.datetime
        3. pd.Timestamp
        4. int -> 自动在右边加 0 然后转换，譬如 '20190302093' --> "2019-03-02"
    params:
        * cursor_date->
            含义: 输入日期
            类型: str
            参数支持: []
    """
    if isinstance(cursor_date, datetime.datetime):
        cursor_date = str(cursor_date)[:10]
    elif isinstance(cursor_date, np.datetime64):
        cursor_date = str(cursor_date)[:10]
    elif isinstance(cursor_date, str):
        try:
            cursor_date = str(pd.Timestamp(cursor_date))[:10]
        except:
            raise ValueError('请输入正确的日期格式, 建议 "%Y-%m-%d"')
    elif isinstance(cursor_date, int):
        cursor_date = str(pd.Timestamp("{:<014d}".format(cursor_date)))[:10]
    else:
        raise ValueError('请输入正确的日期格式，建议 "%Y-%m-%d"')
    return cursor_date


def _init_chinese_rest_days(headers=None):
    global rest_days_df, chinese_holidays_range
    if rest_days_df is None:
        url = os.getenv("TQ_CHINESE_HOLIDAY_URL", "https://files.shinnytech.com/shinny_chinese_holiday.json")
        rsp = requests.get(url, timeout=30, headers=headers)
        chinese_holidays = rsp.json()
        _first_day = datetime.date(int(chinese_holidays[0].split('-')[0]), 1, 1)  # 首个日期所在年份的第一天
        _last_day = datetime.date(int(chinese_holidays[-1].split('-')[0]), 12, 31)  # 截止日期所在年份的最后一天
        chinese_holidays_range = (_first_day, _last_day)
        rest_days_df = pd.DataFrame(data={'date': pd.Series(pd.to_datetime(chinese_holidays, format='%Y-%m-%d'))})
        rest_days_df['trading_restdays'] = False  # 节假日为 False
    return chinese_holidays_range


def get_trading_calendar(start_dt=None, end_dt=None, headers=None):
    """   
    """
    _init_chinese_rest_days(headers=headers)
    df = pd.DataFrame()
    df['date'] = pd.Series(pd.date_range(start=start_dt, end=end_dt, freq="D"))
    df['trading'] = df['date'].dt.dayofweek.lt(5)
    result = pd.merge(rest_days_df, df, sort=True, how="right", on="date")
    result.fillna(True, inplace=True)
    df['trading'] = result['trading'] & result['trading_restdays']
    #df.to_pickle("trade_date_sse.pkl")
    data_to_excel(df, "trade_date_sse")
    return df


def trade_date_sse(start_dt='1990-01-01', end_dt='2030-12-31'):
    if not end_dt:
        end_dt = today()
    #print(type(end_dt))
    try:
        df = read_data_from_excel("trade_date_sse")
        print(df)
    except:
        df = get_trading_calendar(start_dt, end_dt)
        
    td = df[df.trading == True]["date"].values
    td = list(map(lambda x: date2str(x), td))
    return td

#trade_date_cn = trade_date_sse()

if __name__ == "__main__":
    print(read_data_from_excel("trade_date_sse"))

