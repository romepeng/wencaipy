import datetime
import pandas as pd
from pprint import pprint
import requests

from wencaipy.common.wcParameter import (MAX_QUERY_SIZE, QUERY_TYPE,Question_Url,headers_wc,
                                         Drop_columns_ipo, Drop_columns_ipo_2, Fields_basic, Fields_query_etf, Fields_query_index)
from wencaipy.utils.tradeDate import today, if_traded_now, get_real_trade_date, get_last_tradedate
from wencaipy.common.dataToExcel import data_to_excel
from wencaipy.common.wcParameter import Fields_query_condbond
from wencaipy.common.tradeDate import get_real_trade_date, if_traded_now, get_last_tradedate


def fetch_data_from_wencai(trade_date=None, fields_query=None,fields_out=None, query_type=None):
    """ """
    if not trade_date:
        if if_traded_now():
            trade_date = today()
        else:
            trade_date= get_last_tradedate()
    trade_date = get_real_trade_date(trade_date)
    print(trade_date)

    if not fields_query:
        if query_type==QUERY_TYPE().fund:
            fields_query = Fields_query_etf
        if query_type==QUERY_TYPE().stock:
            fields_query = Fields_basic
        if query_type==QUERY_TYPE().bond:
            fields_query=Fields_query_condbond
        if query_type==QUERY_TYPE().index:
            fields_query=Fields_query_index
            
    if not query_type:
        query_type = QUERY_TYPE().stock
        if query_type==QUERY_TYPE().fund:
            fields_query = Fields_query_etf
        if query_type==QUERY_TYPE().stock:
            fields_query = Fields_basic
        if query_type==QUERY_TYPE().bond:
            fields_query=Fields_query_condbond
        if query_type==QUERY_TYPE().index:
            fields_query=Fields_query_index

        
    payload = {
        # 查询问句
        "question": "{},{},上市日期<={}".format(trade_date, ",".join(fields_query), trade_date),
        # 返回查询记录总数 
        "perpage": MAX_QUERY_SIZE,
        "query_type": QUERY_TYPE().stock
    }
    try:
        response = requests.get(Question_Url, params=payload, headers=headers_wc)
        if response.status_code == 200:
            json = response.json()
            df_data = pd.DataFrame(json["data"]["data"])
            print(df_data.columns)
            #print(df_data)
            # 规范返回的columns，去掉[xxxx]内容
            df_data.columns = [col.split("[")[0] for col in df_data.columns]
            #print(df_data)
            # 筛选查询字段，非查询字段丢弃
            if not fields_out:
                if query_type == QUERY_TYPE().stock:
                    try:
                        df = df_data.drop(columns=Drop_columns_ipo)
                    except:
                        df = df_data.drop(columns=Drop_columns_ipo_2)    
                        #print(df)
                else:
                    df = df_data 
            else:
                df = df_data[fields_out]
            # 增加列, 交易日期 code 设置索引、
            dfc = df.copy()
            df = df.assign(trade_date = trade_date) #, code=df["股票代码"].apply(lambda x: x[0:6])).set_index("trade_date", drop=True)
            return df
        else:
            print(f"连接访问接口失败")           
    except Exception as e:
        print(e)


if __name__ == "__main__":
    fields = ["收盘价不复权","成交量", "复权因子"]
    fields = ["最高价创250日新高"]
    fields_out = ["股票代码","股票简称",	"开盘价:不复权","最高价:不复权","最低价:不复权", "收盘价:不复权","成交量", "成交额","复权因子", "新股上市日期"]

    #data_to_excel(fetch_data_from_wencai(trade_date, fields, fields_out),f"stock_daily_{trade_date}")
    #print(fetch_data_from_wencai().columns)
 
    df = fetch_data_from_wencai(trade_date=None,fields_query=["最高价创60日新高"], query_type=QUERY_TYPE.stock)
    print(df)
 
    #print(fetch_data_from_wencai(query_type=QUERY_TYPE().fund))
    #print(fetch_data_from_wencai(query_type=QUERY_TYPE().index))
    #print(fetch_data_from_wencai(query_type=QUERY_TYPE().bond))
    #print(fetch_data_from_wencai(query_type=QUERY_TYPE().stock))
   
    
    
