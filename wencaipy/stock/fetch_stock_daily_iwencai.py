from copy import deepcopy
from dataclasses import Field, field
from pprint import pprint
import requests
import pandas as pd

 
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Upgrade-Insecure-Requests': '1',
        #   'If-Modified-Since': 'Thu, 11 Jan 2018 07:05:01 GMT',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}

headers_wc = deepcopy(headers)
headers_wc["Referer"] = "http://www.iwencai.com/unifiedwap/unified-wap/result/get-stock-pick"
headers_wc["Host"] = "www.iwencai.com"
headers_wc["X-Requested-With"] = "XMLHttpRequest"

Question_url = "http://www.iwencai.com/unifiedwap/unified-wap/result/get-stock-pick"

Fields_all = ['股票代码', '股票简称', 
        '归属母公司股东的净利润(同比增长率)[20220331]', '营业收入(同比增长率)[20220331]',
       '销售毛利率[20220331]', '净资产收益率roe(加权,公布值)[20220331]',
       '新股上市日期',
       '预测净资产收益率(roe)平均值[20221231]', '预测净资产收益率(roe)平均值[20231231]',
       '预测净资产收益率(roe)平均值[20241231]', '归属于母公司所有者的净利润[20220331]',
       '股东权益合计[20220331]', 
       '所属同花顺行业', '所属同花顺行业',
       '申购日期', '单账户顶格', '公开发行市值', '网上发行数量','网下发行数量', '网上有效申购户数', '上市板块', '新股主承销商', '网上中签结果公告日', '招股说明书', '打新技巧',
       '营业收入[20220331]', '预测主营业务收入增长率[20221231]', '最新价', '最新涨跌幅', 'hqCode', 'marketId']

        
Fields_common = ["股票简称", "股票代码", '最新价',"市盈率(pe)", "市净率(pb)", '总股本',
      
       "所属申万行业",'所属同花顺行业']


def fetch_stock_daily_wencai(trade_date, fields_out=None):
    """通过问财接口抓取数据
    Arguments:
        trade_date {[type]} -- [description]
        fields {[type]} -- [description]
    Returns:
        [type] -- [description]
    """
    fields = ["收盘价不复权","成交量", "复权因子"]
    fields_out = ["股票代码","股票简称",	"开盘价:不复权","最高价:不复权","最低价:不复权", "收盘价:不复权","成交量", "成交额","复权因子", "新股上市日期"]
    payload = {
        # 查询问句
        "question": "{},{},上市日期<={}".format(trade_date, ",".join(fields), trade_date),
        # 返回查询记录总数 
        "perpage": 6000,
        "query_type": "stock"
    }
    try:
        response = requests.get(Question_url, params=payload, headers=headers_wc)
        if response.status_code == 200:
            json = response.json()
            df_data = pd.DataFrame(json["data"]["data"])
            print(df_data.columns)
            #print(df_data)
            # 规范返回的columns，去掉[xxxx]内容
            df_data.columns = [col.split("[")[0] for col in df_data.columns]
            # 筛选查询字段，非查询字段丢弃
            df = df_data[fields_out]
            # 增加列, 交易日期 code 设置索引
            df = df.assign(trade_date=trade_date, code=df["股票代码"].apply(lambda x: x[0:6])).set_index("trade_date", drop=True)
            return df
        else:
            print("连接访问接口失败")           
    except Exception as e:
        print(e)


def fetch_stock_finance_from_wencai(trade_date, fields):
    """通过问财接口抓取数据
    Arguments:
        trade_date {[type]} -- [description]
        fields {[type]} -- [description]
    Returns:
        [type] -- [description]
    """
    fields = ['归属母公司股东的净利润(同比增长率)', '营业收入(同比增长率)','销售毛利率','净资产收益率roe',"所属申万行业"]
    print(fields)
    payload = {
        # 查询问句
        "question": "{},{},上市日期<={}".format(trade_date, ",".join(fields), trade_date),
        # 返回查询记录总数 
        "perpage": 6000,
        "query_type": "stock"
    }
    try:
        response = requests.get(Question_url, params=payload, headers=headers_wc)
        if response.status_code == 200:
            json = response.json()
            df_data = pd.DataFrame(json["data"]["data"])
            print(df_data.columns)
            #print(df_data)
            # 规范返回的columns，去掉[xxxx]内容
            df_data.columns = [col.split("[")[0] for col in df_data.columns]
            # 筛选查询字段，非查询字段丢弃
            df = df_data  #[fields] if fields else df_data
            # 增加列, 交易日期 code 设置索引
            df = df.assign(trade_date=trade_date, code=df["股票代码"].apply(lambda x: x[0:6])).set_index("trade_date", drop=False)
            return df
        else:
            print("连接访问接口失败")           
    except Exception as e:
        print(e)


if __name__ == "__main__":
    from rrdata.utils.rqDate_trade import rq_util_get_last_tradedate
    trade_date = rq_util_get_last_tradedate()
    df = fetch_stock_daily_wencai(trade_date)
    print(df)
    df.to_excel("/mnt/f/Stock/iwencai/daily_2.xlsx")

    #df2 = fetch_stock_finance_from_wencai(trade_date,[])
    #pprint(df2)
    #df2.to_excel('/mnt/f/Stock/iwencai/finance.xlsx')
