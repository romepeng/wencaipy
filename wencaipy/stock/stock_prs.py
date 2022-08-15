import time
import pandas as pd 
from wencaipy.common.fetch_base_wencai import fetch_data_from_wencai
from wencaipy.common.wcParameter import QUERY_TYPE, PERIODS, PERIODS_LIST
from wencaipy.common.dataToExcel import data_to_excel
from wencaipy.utils.tradeDate import get_real_trade_date


def stock_industry_concept(trade_date=None):
   Fields_Query = ["申万行业","概念"]
   df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().stock)
   print(df.columns)
   """
   ['股票代码', '股票简称', '所属申万行业', '所属概念', '新股上市日期', '所属概念数量', 'a股市值(不含限售股)',
       '所属同花顺行业', '最新dde大单净额', '总股本', '市盈率(pe)', '最新价', '最新涨跌幅', 'trade_date']
   """
   df.columns = ['sec_code', 'sec_name', 'swl', 'concept', 'list_date', 'concept_num', 'fmv', \
      'thsl ', 'dde', 'total_shares',  'pe', 'close', 'pct_chg', 'trade_date']
   data_to_excel(df, "stock_industry_concept")
   return df


def stock_ma():
    Fields_ma_query =  ["5日均线", "10日均线","20日均线","60日均线","120日均线","250日均线"]
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_ma_query, query_type=QUERY_TYPE().stock)
    """
    df.columns = ['股票代码', '股票简称', '5日均线', '10日均线', '20日均线', '60日均线', '120日均线', '250日均线',
       '新股上市日期', '买入信号inter', '技术形态', '所属同花顺行业', '最新价', '最新涨跌幅', 'trade_date']
    """
    #print(df.columns)
    df.columns = ['sec_code', 'sec_name', 'ma5', 'ma10', 'ma20', 'ma60', 'ma120', 'ma250',
       'list_date', 'buy_flag', 'technical_status', 'thsl', 'close', 'pct_chg', 'trade_date']
    data_to_excel(df, "stock_ma")
    return df


def stock_oh_ol(period=250):
   """
   fields_in:  
   ['股票代码', '股票简称', '收盘价:不复权[20220718]', '历史最高价前复权',
       '{(}收盘价:不复权[20220718]{/}历史最高价前复权{)}', '区间最高价:前复权[20210707-20220718]',
       '区间最高价:前复权日[20210707-20220718]',
       '{(}收盘价:不复权[20220718]{/}区间最高价:前复权[20210707-20220718]{)}',
       '区间最低价:前复权[20210707-20220718]', '区间最低价:前复权日[20210707-20220718]',
       '{(}收盘价:不复权[20220718]{/}区间最低价:前复权[20210707-20220718]{)}', '新股上市日期',
       '开盘价:不复权[20220718]', '最高价:不复权[20220718]', '最低价:不复权[20220718]', '申购日期',
       '单账户顶格', '公开发行市值', '网上发行数量', '网下发行数量', '网上有效申购户数', '上市板块', '新股主承销商',
       '网上中签结果公告日', '招股说明书', '打新技巧', '所属同花顺行业', '最新涨跌幅', 'hqCode', 'marketId']
   field_out:   
   ['股票代码', '股票简称', '收盘价:不复权', '历史最高价前复权', '{(}收盘价:不复权', '区间最高价:前复权',
       '区间最高价:前复权日', '{(}收盘价:不复权', '区间最低价:前复权', '区间最低价:前复权日', '{(}收盘价:不复权',
       '新股上市日期', '开盘价:不复权', '最高价:不复权', '最低价:不复权', '所属同花顺行业', '最新涨跌幅',
       'trade_date']
   """ 
   Fields_high_period = ["历史最高价","250日最高价"]
   Fields_high_period_chg = ["股价/历史最高价","股价/250日最高价","股价/250日最低价"]
   Fields_high_period_out = ['股票代码', '股票简称', '收盘价:不复权', '历史最高价前复权', '{(}收盘价:不复权', '区间最高价:前复权',
       '区间最高价:前复权日', '{(}收盘价:不复权', '区间最低价:前复权', '区间最低价:前复权日', '{(}收盘价:不复权',
       '新股上市日期', '开盘价:不复权', '最高价:不复权', '最低价:不复权', '所属同花顺行业', '最新涨跌幅',
       'trade_date']
   df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_high_period_chg, query_type=QUERY_TYPE().stock)
   """
    df.columns = ['股票代码', '股票简称', '收盘价', '历史最高价', '收盘价/历史最高价', '区间最高价',
       '区间最高价日', '收盘价/区间最高价', '区间最低价', '区间最低价日', '收盘价/区间最低价日',
       '新股上市日期', '开盘价', '最高价', '最低价', '所属同花顺行业', '最新涨跌幅', 'trade_date']
   """
   #print(df)
   #print(df.columns)
   df = df[['股票代码', '股票简称', '收盘价:不复权', '历史最高价前复权', '{(}收盘价:不复权', 
            '区间最高价:前复权', '区间最高价:前复权日',  '区间最低价:前复权', '区间最低价:前复权日', 
       '新股上市日期', '开盘价:不复权', '最高价:不复权', '最低价:不复权', '所属同花顺行业', '最新涨跌幅',
       'trade_date']]

   df.columns = ['sec_code', 'sec_name', 'close', 'H_0', 'OH_0',f'OH_{period}',  f'OL_{period}',
                 f'H_{period}', f'date_H_{period}',   f'L_{period}',f'date_L_{period}',
               'list_date', 'open', 'high', 'low', 'thsl', 'pch_chg', 'trade_date']
   #print(df.columns)
   df['OH_0'] = 100 *  df['OH_0'] 
   df[f'OH_{period}']=  100 * df[f'OH_{period}']
   df[f'OL_{period}'] =   100 * (df[f'OL_{period}'] - 1)
   data_to_excel(df, f"stock_high_low_chg_{period}")
   return df


def stock_rt():
    """ """
    Fields_industry = ["所属申万行业",'所属同花顺行业']
    Fields_return_query =  ["5日涨幅", "10日涨幅","20日涨幅","60日涨幅","120日涨幅","250日涨幅"]
    Fields_Query =  Fields_industry  + Fields_return_query
    #print(Fields_Query)
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().stock)
    df.columns = ['股票代码', '股票简称','所属申万行业', '所属同花顺行业',
                "5日涨幅", "10日涨幅","20日涨幅","60日涨幅","120日涨幅","250日涨幅",       
                "新股上市日期",'最新dde大单净额', '所属概念','最新价', '最新涨跌幅','trade_date']
    data_to_excel(df, "stock_rt")
    return df


def stock_vol_chg(period_vol=50):
    Fields_Query = [f"成交量/{period_vol}日成交均量"]
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().stock)
    """
    df.columns = ['股票代码', '股票简称', '成交量', f'{period}日均成交量', f'成交量变化_{period}', '新股上市日期', '涨跌幅:前复权', '涨跌',
       '振幅', '成交额', '所属同花顺行业', f'{period}日成交量', f'{period}日换手率', '最新价', '最新涨跌幅', 'trade_date']
    #print(df.columns)
    """
    df.columns = ['sec_code', 'sec_name', 'vol', f'vol_ma{period_vol}', f'vol_chg{period_vol}', 'list_date', 'pct_chg', 'change',
       'amplitude ', 'amount', 'thsl', f'vol{period_vol}', f'turnover{period_vol}', 'close', 'pct_chg', 'trade_date']
    data_to_excel(df, f"stock_vol_chg_{period_vol}")
    return df


def stock_prs():
    """ """
    Fields_industry = ["所属申万行业",'所属同花顺行业','市值']
    Fields_return_query =  ["5日涨幅", "10日涨幅","20日涨幅","60日涨幅","120日涨幅","250日涨幅"]
    Fields_Query =  Fields_industry  + Fields_return_query
    #print(Fields_Query)
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().stock)
    df.columns = ['股票代码', '股票简称','所属申万行业', '所属同花顺行业',"总市值",
                "5日涨幅", "10日涨幅","20日涨幅","60日涨幅","120日涨幅","250日涨幅",       
                "新股上市日期",'流通市值', '最新价', '最新涨跌幅','trade_date']
    df.columns = ['sec_code', 'sec_name','swl', 'thsl',"tmv"] + PERIODS_LIST().RT_LIST + ["list_date",'fmv', 'close', 'pct_chg','trade_date']
    for i in PERIODS().PERIODS:
        df[f"rs{i}"] = 100*df[f"rt{i}"].rank(axis=0,ascending=True, pct=True)
    data_to_excel(df, "stock_prs")
    return df


def stock_revenue_inc(years=3):
    """
    ['股票代码', '股票简称', '营业收入(同比增长率)', '营业收入(同比增长率)', '营业收入(同比增长率)',
       '营业收入(同比增长率)', '新股上市日期', '所属同花顺行业', '营业收入', '营业收入', '营业收入', '营业收入',
       '预测主营业务收入增长率', '最新价', '最新涨跌幅', 'trade_date']
    """
    Fields_query_inc = ["3年收入同比增长率"]
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_query_inc, query_type=QUERY_TYPE().stock)
    #print(df.columns)
    df.columns = ['sec_code', 'sec_name', 'revenue_inc_0', 'revunue_inc_L', 'revenue_inc_B','revenue_inc_BL',
    'list_date', 'thsl',  'revenue_inc_0','revunue_L', 'revenue_B','revenue_BL',
       'revenue_inc_forecast', 'close', 'pct_chg', 'trade_date']
    df = df[['sec_code', 'sec_name', 'revunue_inc_L', 'revenue_inc_B','revenue_inc_BL',
    'list_date', 'thsl', 'revunue_L', 'revenue_B','revenue_BL',
       'revenue_inc_forecast', 'close', 'pct_chg', 'trade_date']]
   
    data_to_excel(df, f"stock_revenue_inc_{years}years")
    return df


def stock_quarter_inc(quarters=4): #TODO
    """
    ['股票代码', '股票简称', '归属母公司股东的净利润(同比增长率)', '归属母公司股东的净利润(同比增长率)',
       '归属母公司股东的净利润(同比增长率)', '归属母公司股东的净利润(同比增长率)', '归属母公司股东的净利润(同比增长率)',
       '新股上市日期', '所属同花顺行业', '营业收入(同比增长率)', '营业收入(同比增长率)', '营业收入(同比增长率)',
       '营业收入(同比增长率)', '最新价', '最新涨跌幅', 'trade_date']
    
    """
    Fields_query_inc = ["4个季度的净利润同比增长率"]
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_query_inc, query_type=QUERY_TYPE().stock)
    print(df.columns)
   
    df.columns = ['sec_code', 'sec_name', 
                  'netProfit_Q_inc_0', 'netProfit_Q1_inc','netProfit_Q2_inc','netProfit_Q3_inc','netProfit_Q4_inc',
                'list_date', 'thsl',
                'revunue_Q1_inc', 'revenue_Q2_inc','revenue_Q3_inc','revenue_Q4_inc',
                'close', 'pct_chg', 'trade_date']

    df = df[['sec_code', 'netProfit_Q1_inc','netProfit_Q2_inc','netProfit_Q3_inc','netProfit_Q4_inc',
             'revunue_Q1_inc', 'revenue_Q2_inc','revenue_Q3_inc','revenue_Q4_inc']]
   
    data_to_excel(df, f"stock_income_inc_last{quarters}quarters")
    return df


def stock_year_inc(years=3):
    """
    ['股票代码', '股票简称', '归属母公司股东的净利润(同比增长率)', '归属母公司股东的净利润(同比增长率)',
       '归属母公司股东的净利润(同比增长率)', '归属母公司股东的净利润(同比增长率)', 
       '新股上市日期', '所属同花顺行业',
       'revenue_inc_0', 'revunue_inc_L', 'revenue_inc_B','revenue_inc_BL'
       #'营业收入(同比增长率)', '营业收入(同比增长率)', '营业收入(同比增长率)', '营业收入(同比增长率)',
       '销售毛利率', '最新价', '最新涨跌幅', 'trade_date']
    """
    Fields_query_inc = ["3年的利润同比增长率"]
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_query_inc, query_type=QUERY_TYPE().stock)
    #print(df.columns)
    df.columns = ['sec_code', 'sec_name', 'netProfit_inc_0', 'netProfit_inc_L','netProfit_inc_B','netProfit_inc_BL',
       'list_date', 'thsl',
       'revenue_inc_0', 'revunue_inc_L', 'revenue_inc_B','revenue_inc_BL',
       'gpr', 'close', 'pct_chg', 'trade_date']
       
    df = df[['sec_code', 'sec_name', 'netProfit_inc_L','netProfit_inc_B','netProfit_inc_BL',
       'list_date', 'thsl',
        'revunue_inc_L', 'revenue_inc_B','revenue_inc_BL',
        'close', 'pct_chg', 'trade_date']]
    data_to_excel(df, f"stock_income_inc_last{years}years")
    return df


def stock_forecast():
    """ in: 
     预告净利润(all stock)
    out:
    ['股票代码', '股票简称', '预告净利润', '新股上市日期', '业绩预告类型', '上年同期净利润', '预告净利润变动幅度',
       '业绩预告日期', '业绩变化原因', '业绩预告摘要', '预告净利润上限', '预告净利润下限', 
       '所属同花顺行业', '最新价',   '最新涨跌幅', 'trade_date']
    in:业绩预告日期不为空(forecasted stock) 
    out:['股票代码', '股票简称', '业绩预告日期', '新股上市日期', '所属同花顺行业', '业绩预告类型', '预告净利润',
       '上年同期净利润', '预告净利润变动幅度', '业绩变化原因', '业绩预告摘要', '最新价', '最新涨跌幅',
       'trade_date']
    """
    Fields_Query = ["预告净利润"]
    df = fetch_data_from_wencai(trade_date=None,fields_query=Fields_Query,fields_out=None, query_type=QUERY_TYPE.stock)
    print(df.columns)
    df.columns = ['sec_code','sec_name','forecast_netProfit','list_date','forecast_type','last_year_netProfit','forecast_netProfit_pctchg',
     'date_forecast','change_reason','forcast_sammury',  'forecast_netProfit_uplimit', 'forecast_netProfit_downlimit',
            'thsl','close','pct_chg','trade_date']
    df.sort_values(by='date_forecast', ascending=False, inplace=True)
    data_to_excel(df, f"stock_forecast")
    return df


def stock_prs_oh_ol_volchg_inc(period=250, period_vol=50,period_history=0):
    df_prs = stock_prs()
    df_ma = stock_ma()[['sec_code','ma5', 'ma10', 'ma20', 'ma60', 'ma120', 'ma250']]
    df_vol = stock_vol_chg(period_vol=period_vol)[['sec_code',  'vol', f'vol_ma{period_vol}', f'vol_chg{period_vol}', 'amount', f'vol{period_vol}', f'turnover{period_vol}']]
    df_oh = stock_oh_ol(period=period)[['sec_code',  'H_0', 'OH_0', f'H_{period}',
       f'date_H_{period}', f'OH_{period}', f'L_{period}', f'date_L_{period}', f'OL_{period}',
       'open', 'high', 'low']]
    df_inc = stock_year_inc()[['sec_code','netProfit_inc_L','netProfit_inc_B','netProfit_inc_BL',
                                 'revunue_inc_L', 'revenue_inc_B','revenue_inc_BL']]
    df = pd.merge(df_prs, df_ma, on="sec_code")
    df = pd.merge(df, df_vol, on="sec_code")
    df = pd.merge(df, df_oh, on="sec_code")
    df = pd.merge(df, df_inc, on="sec_code")
    #print(df.columns)
    df = df[['trade_date','sec_code', 'sec_name', 'swl', 'thsl', 'tmv','fmv','rt5', 'rt10', 'rt20',
       'rt60', 'rt120', 'rt250', 'list_date',  'close', 'open', 'high',
       'low','pct_chg',
        'rs5', 'rs10', 'rs20', 'rs60', 'rs120', 'rs250',
        'ma5', 'ma10', 'ma20', 'ma60', 'ma120', 'ma250', 
        'vol', 'vol_ma50','vol_chg50', 'amount', 'vol50', 'turnover50', 
        'H_0', 'OH_0', 'H_250','date_H_250', 'OH_250', 'L_250', 'date_L_250', 'OL_250',
        'netProfit_inc_L','netProfit_inc_B','netProfit_inc_BL',
        'revunue_inc_L', 'revenue_inc_B','revenue_inc_BL']]
    data_to_excel(df, f'stock_prs_oh_volchg_inc_{get_real_trade_date()}')
    return df
 
 
def stock_prs_oh_ol_volchg_inc_concept(period=250, period_vol=50,period_history=0):
    df_prs = stock_prs()
    df_ma = stock_ma()[['sec_code','ma5', 'ma10', 'ma20', 'ma60', 'ma120', 'ma250']]
    df_vol = stock_vol_chg(period_vol=period_vol)[['sec_code',  'vol', f'vol_ma{period_vol}', f'vol_chg{period_vol}', 'amount', f'vol{period_vol}', f'turnover{period_vol}']]
    df_oh = stock_oh_ol(period=period)[['sec_code',  'H_0', 'OH_0', f'H_{period}',
       f'date_H_{period}', f'OH_{period}', f'L_{period}', f'date_L_{period}', f'OL_{period}',
       'open', 'high', 'low']]
    df_inc = stock_year_inc()[['sec_code','netProfit_inc_L','netProfit_inc_B','netProfit_inc_BL',
                                 'revunue_inc_L', 'revenue_inc_B','revenue_inc_BL']]
    df_concept = stock_industry_concept()[['sec_code','concept']]
    df = pd.merge(df_prs, df_ma, on="sec_code")
    df = pd.merge(df, df_vol, on="sec_code")
    df = pd.merge(df, df_oh, on="sec_code")
    df = pd.merge(df, df_inc, on="sec_code")
    df = pd.merge(df,df_concept, on="sec_code")
    #print(df.columns)
    df = df[['trade_date','sec_code', 'sec_name', 'swl', 'thsl', 'concept','tmv','fmv','rt5', 'rt10', 'rt20',
       'rt60', 'rt120', 'rt250', 'list_date',  'close', 'open', 'high',
       'low','pct_chg',
        'rs5', 'rs10', 'rs20', 'rs60', 'rs120', 'rs250',
        'ma5', 'ma10', 'ma20', 'ma60', 'ma120', 'ma250', 
        'vol', 'vol_ma50','vol_chg50', 'amount', 'vol50', 'turnover50', 
        'H_0', 'OH_0', 'H_250','date_H_250', 'OH_250', 'L_250', 'date_L_250', 'OL_250',
        'netProfit_inc_L','netProfit_inc_B','netProfit_inc_BL',
        'revunue_inc_L', 'revenue_inc_B','revenue_inc_BL']]
    data_to_excel(df, f'stock_prs_oh_volchg_inc_concept_{get_real_trade_date()}')
    return df


 
def stock_prs_oh_ol_volchg_inc_forecast_concept(period=250, period_vol=50,period_history=0):
    df_prs = stock_prs()
    df_ma = stock_ma()[['sec_code','ma5', 'ma10', 'ma20', 'ma60', 'ma120', 'ma250']]
    df_vol = stock_vol_chg(period_vol=period_vol)[['sec_code',  'vol', f'vol_ma{period_vol}', f'vol_chg{period_vol}', 'amount', f'vol{period_vol}', f'turnover{period_vol}']]
    df_oh = stock_oh_ol(period=period)[['sec_code',  'H_0', 'OH_0', f'H_{period}',
       f'date_H_{period}', f'OH_{period}', f'L_{period}', f'date_L_{period}', f'OL_{period}'
       ]]
    df_inc = stock_year_inc()[['sec_code','netProfit_inc_L','netProfit_inc_B','netProfit_inc_BL',
                                 'revunue_inc_L', 'revenue_inc_B','revenue_inc_BL']]
    df_concept = stock_industry_concept()[['sec_code','concept']]
    df_forecast = stock_forecast()[['sec_code','forecast_netProfit_pctchg']]
    df = pd.merge(df_prs, df_ma, on="sec_code")
    df = pd.merge(df, df_vol, on="sec_code")
    df = pd.merge(df, df_oh, on="sec_code")
    df = pd.merge(df, df_inc, on="sec_code")
    df = pd.merge(df,df_concept, on="sec_code")
    df = pd.merge(df, df_forecast, on='sec_code')
    #print(df.columns)
    df = df[['trade_date','sec_code', 'sec_name', 'swl', 'thsl', 'concept','tmv','fmv','rt5', 'rt10', 'rt20',
       'rt60', 'rt120', 'rt250', 'list_date',  'close', 'pct_chg',
        'rs5', 'rs10', 'rs20', 'rs60', 'rs120', 'rs250',
        'ma5', 'ma10', 'ma20', 'ma60', 'ma120', 'ma250', 
        'vol', 'vol_ma50','vol_chg50', 'amount', 'vol50', 'turnover50', 
        'H_0', 'OH_0', 'H_250','date_H_250', 'OH_250', 'L_250', 'date_L_250', 'OL_250',
        'netProfit_inc_L','netProfit_inc_B','netProfit_inc_BL',
        'revunue_inc_L', 'revenue_inc_B','revenue_inc_BL','forecast_netProfit_pctchg']]
    data_to_excel(df, f'stock_prs_oh_volchg_inc_forecast_concept_{get_real_trade_date()}')
    return df
    

if __name__ == "__main__":
    #print(stock_industry_concept())
    #print(stock_ma())
    #print(stock_oh_ol()) 
    #print(stock_vol_chg())
    
    #print(stock_prs())

    #print(stock_year_inc())
    #print(stock_quarter_inc())
    #print(stock_forecast())
    
    #print(stock_prs_oh_ol_volchg_inc())
    #print(stock_prs_oh_ol_volchg_inc_concept())
    print(stock_prs_oh_ol_volchg_inc_forecast_concept())
    
    
    
    