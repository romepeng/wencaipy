from wencaipy.common.fetch_base_wencai import fetch_data_from_wencai
from wencaipy.common.wcParameter import QUERY_TYPE
from wencaipy.common.dataToExcel import data_to_excel



def fetch_ths_all_index_prs():
    """ 同花顺板块指数 :764 同花顺行业指数 同花顺特色指数  同花顺概念指数 同花顺地域指数"""
    Fields_Query_ths_level3 = ["同花顺板块指数"]
    Fields_return_query =  ["5日涨幅", "10日涨幅","20日涨幅","60日涨幅","120日涨幅","250日涨幅"]
    Fields_Query =  Fields_Query_ths_level3 + Fields_return_query
    #print(Fields_Query)
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().index)
    df.columns = ['指数代码', '指数简称', '指数@同花顺板块指数', 
                "5日涨幅", "10日涨幅","20日涨幅","60日涨幅","120日涨幅","250日涨幅",       
               '指数@收盘价:不复权', '指数@涨跌幅:前复权',
                'hqCode','marketId','trade_date']
    data_to_excel(df, "ths_all_index_rt")
    return df



def fetch_ths_level3_index_prs():
    """ 同花顺板块指数 :764 同花顺行业指数 同花顺特色指数  同花顺概念指数 同花顺地域指数"""
    Fields_Query_ths_level3 = ["同花顺板块指数","三级行业"]
    Fields_return_query =  ["5日涨幅", "10日涨幅","20日涨幅","60日涨幅","120日涨幅","250日涨幅"]
    Fields_Query =  Fields_Query_ths_level3 + Fields_return_query
    print(Fields_Query)
    df = fetch_data_from_wencai(trade_date=None, fields_query=Fields_Query,query_type=QUERY_TYPE().index)
    df.columns = ['指数代码', '指数简称', '指数@同花顺板块指数', '指数@所属同花顺行业级别',
                "5日涨幅", "10日涨幅","20日涨幅","60日涨幅","120日涨幅","250日涨幅",       
                '指数@同花顺行业指数', '指数@收盘价:不复权', '指数@涨跌幅:前复权',
                'hqCode','marketId','trade_date']
    data_to_excel(df, "ths_level3_index_rt")
    return df


if __name__ == "__main__":
    print(fetch_ths_all_index_prs())
    print(fetch_ths_level3_index_prs())
    