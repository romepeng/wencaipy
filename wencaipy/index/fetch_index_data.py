from dataclasses import Field
from turtle import pd
from wencaipy.common.fetch_base_wencai import fetch_data_from_wencai
from wencaipy.common.wcParameter import QUERY_TYPE
from wencaipy.common.dataToExcel import data_to_excel


def fetch_ths_sector_index():
    """ 同花顺板块指数 :764 同花顺行业指数 同花顺特色指数  同花顺概念指数 同花顺地域指数"""
    Fields_Query = ["同花顺板块指数"]
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().index)
    data_to_excel(df, "ths_all_index")
    return df

def fetch_ths_industry_level3_index():
    """ 同花顺板块指数 :764 同花顺行业指数 同花顺特色指数  同花顺概念指数 同花顺地域指数"""
    Fields_Query = ["同花顺板块指数","三级行业"]
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().index)
    data_to_excel(df, "ths_level3_index")
    return df

def fetch_ths_area_index():
    """ 同花顺板块指数 :764 同花顺行业指数 同花顺特色指数  同花顺概念指数 同花顺地域指数"""
    Fields_Query = ["同花顺板块指数","同花顺地域指数"]
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().index)
    data_to_excel(df, "ths_area_index")
    return df

def fetch_ths_concept_index():
    """ 同花顺板块指数 :  同花顺概念指数 """
    Fields_Query = ["同花顺板块指数","同花顺概念指数"]
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().index)
    data_to_excel(df, "ths_concept_index")
    return df


def index_ths_level3_rt():
    """ 同花顺板块指数 :764 同花顺行业指数 同花顺特色指数  同花顺概念指数 同花顺地域指数"""
    Fields_Query_index = ["同花顺行业指数","三级行业"]
    Fields_return_query =  ["5日涨幅","10日涨幅","20日涨幅","60日涨幅","120日涨幅","250日涨幅"]
    Fields_Query = Fields_Query_index + Fields_return_query
    print(Fields_Query)
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().index)
    print(df.columns)
    data_to_excel(df, "ths_level3_index_rt")
    return df


def index_industry_sw_ths_all():
    Fields_Query = ["申万行业指数"]
    Fields_swl = ["股票简称", "股票代码", "市盈率(pe)",  "所属申万行业",'所属同花顺行业']
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query, fields_out=Fields_swl ,query_type=QUERY_TYPE().stock)
    #print(df.columns)
    df.columns = ['sec_name','sec_code','pe','swl','thsl','trade_date']
    data_to_excel(df, "index_industry_all")
    return df


def swl_level():
    Fields_Query = ["申万行业指数"]
    Fields_swl = ["股票简称", "股票代码", "市盈率(pe)",  "所属申万行业",'所属同花顺行业']
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query, fields_out=Fields_swl ,query_type=QUERY_TYPE().stock)
    #print(df.columns)
    df.columns = ['sec_name','sec_code','pe','swl','thsl','trade_date']
    df = df[['swl']]
    df = df.drop_duplicates()
    return df 


def swl_index_components(level="L3"): # TODO
    """['股票代码', '股票简称', '所属申万行业', '新股上市日期', '最新dde大单净额', '所属概念', '总股本',
       '市盈率(pe)', '最新价', '最新涨跌幅', 'trade_date']
    """
    Fields_Query = ["所属申万行业"]
    Fields_inustry = ["股票代码","股票简称", '所属申万行业']
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query, fields_out=None, query_type=QUERY_TYPE().stock)
    #print(df.columns)
    df = df[Fields_inustry]
    df.columns = ['sec_code','sec_name','swl']
    #print(df)
    df["swl_name_L3"] = df['swl'].apply(lambda x : list(str(x).split("--"))[-1] + f"_{level}")
    data_to_excel(df, "index_swl_index_components")
    swl_L3 = list(set(df['swl_name_L3'].values))
    swl_l3_dict = dict()
    for l in swl_L3:
        swl_l3_dict.keys = l
        swl_l3_dict.values = df[df["swl_name_L3"] == l].sec_name.values
    print(swl_l3_dict)
    return df 


def thsl_index_components():
    """['股票代码', '股票简称', '所属同花顺行业', '新股上市日期', '最新dde大单净额', '所属概念', '总股本',
       '市盈率(pe)', '最新价', '最新涨跌幅', 'trade_date']
    """
    Fields_Query = ["同花顺行业"]
    Fields_inustry = ["股票简称", "股票代码", '所属同花顺行业']
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query, fields_out=Fields_inustry, query_type=QUERY_TYPE().stock)
    print(df.columns)
    df.columns = ['sec_name','sec_code','thsl','trade_date']
    for level in ["L1","L2","L3"]:
        l = int(level[-1]) - 1
        col = str(f"thsl_name_{level}")
        #print(level, l, col)
        df[col] = df['thsl'].apply(lambda x : x.split("-")[l] + f"_{level}")
    data_to_excel(df, "index_thsl_index_components")
    return df 


def index_thsl_valuation(level="L3"):
    """_summary_
    ['指数代码', '指数简称', '指数@同花顺行业指数', '指数@所属同花顺行业级别', '指数@市盈率', '指数@阶段最新市盈率日',
       '指数@阶段最新市盈率', '指数@市净率', '指数@市现率', '指数@市销率', '指数@收盘价:不复权', '指数@涨跌幅:前复权',
       'hqCode', 'marketId', 'trade_date']
    Args:
        level (str, optional): _description_. Defaults to "L3".
    Returns:
    ['指数代码', '指数简称',  ' 指数@所属同花顺行业级别', '指数@市盈率', '指数@阶段最新市盈率日',
       '指数@阶段最新市盈率', '指数@市净率', '指数@市现率', '指数@市销率', '指数@收盘价:不复权', '指数@涨跌幅:前复权',
        'trade_date']
        _type_: _description_
    """
    if level == "L2":
        Fields_Query = ["同花顺行业指数","二级行业","pe"]
    elif level == "L3":
        Fields_Query = ["同花顺行业指数","三级行业","pe"]
    Fields_index_out  =   ['指数代码', '指数简称',  '指数@所属同花顺行业级别', '指数@市盈率', '指数@阶段最新市盈率日',
       '指数@阶段最新市盈率', '指数@市净率', '指数@市现率', '指数@市销率', '指数@收盘价:不复权', '指数@涨跌幅:前复权']
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query, fields_out=Fields_index_out ,query_type=QUERY_TYPE().index)
    #print(df.columns)
    df.columns = ['index_code','index_name','level_cn','pe','pe_date','pe_new','pb','pc','ps','close','pct_chg','trade_date']
    df_out = df.copy()
    df_out['level'] = level
    df_out= df_out[['index_code','index_name','level','pe','pb','pc','ps','close','pct_chg','trade_date']]
    data_to_excel(df_out, f"index_thsl_valuation_{level}")
    return df_out 


if __name__ == "__main__":
    
    #print(fetch_ths_sector_index())
    #print(fetch_ths_industry_level3_index())
    #print(fetch_ths_area_index())
    #print(fetch_ths_concept_index())
    #print(index_ths_level3_rt())
    #print(index_industry_sw_ths_all())
    #print(swl_level())
    #print(thsl_index_components())
    #print(index_thsl_valuation("L3"))
    print(swl_index_components())