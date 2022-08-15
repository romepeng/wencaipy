from copy import deepcopy
from enum import Enum
from pytz import timezone
import os


CHINA_TZ = timezone("Asia/Shanghai")

PATH_HOME = os.path.expanduser("~")

SQLITE_PATH_RR_PC = "/mnt/f/Stock/iwencai/"

SQLITE_PATH_ALIYUN = "/mnt/disk1/sqlit_data/"
PATH_WSL_IWENCAI =  "/mnt/f/Stock/iwencai/"

PATH_ALIYUN_IWENCAI = "/mnt/disk1/stock/iwencai/"

PATH_VPS_IWENCAI = f"{PATH_HOME}/data/iwencai/"

MAX_QUERY_SIZE: int = 6000
WC_DATE_FORMATE: str = '%Y-%m-%d'
MAX_QUERY_TIMES: int = 500


HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}

headers_wc = deepcopy(HEADERS)
#headers_wc["Referer"] = "http://www.iwencai.com/unifiedwap/unified-wap/result/get-stock-pick"
headers_wc["Referer"] = "http://www.iwencai.com/unifiedwap/"
headers_wc["Host"] = "www.iwencai.com"
headers_wc["X-Requested-With"] = "XMLHttpRequest"


Question_Url = "http://www.iwencai.com/unifiedwap/unified-wap/result/get-stock-pick"

Fields_all = ['股票代码', '股票简称', '最新价', '最新涨跌幅',
        '归属母公司股东的净利润(同比增长率)', '营业收入(同比增长率)',
       '销售毛利率', '净资产收益率roe(加权,公布值)',
       '新股上市日期',

       '营业收入','归属于母公司所有者的净利润', '股东权益合计',
       '所属同花顺行业', '所属同花顺行业',

       '申购日期', '单账户顶格', '公开发行市值', '网上发行数量','网下发行数量', '网上有效申购户数', '上市板块', '新股主承销商', '网上中签结果公告日', '招股说明书', '打新技巧',

        '预测净资产收益率(roe)平均值[20221231]', '预测净资产收益率(roe)平均值[20231231]',   '预测净资产收益率(roe)平均值[20241231]',
        '预测主营业务收入增长率[20221231]',
        'hqCode', 'marketId']

Fields_out = ['股票代码', '股票简称','最新价', '最新涨跌幅','所属同花顺行业']

Drop_columns_ipo = ['申购日期', '单账户顶格', '公开发行市值', '网上发行数量','网下发行数量', '网上有效申购户数', '上市板块',
                             '新股主承销商', '网上中签结果公告日','招股说明书', '打新技巧','hqCode', 'marketId']
Drop_columns_ipo_2 = ['申购日期', '单账户顶格', '公开发行市值', '网上发行数量', '网下发行数量', '网上有效申购户数', '上市板块',
                            '新股主承销商','hqCode','marketId']

Fields_Incease = ['股票代码', '股票简称', '营业收入(同比增长率)','归属母公司股东的净利润(同比增长率)', '销售毛利率',"所属申万行业"]

Fields_common = ["股票简称", "股票代码", '最新价',"市盈率(pe)", "市净率(pb)", '总股本', "所属申万行业",'所属同花顺行业']

Fields_daily = ["股票代码","股票简称",	"开盘价:不复权","最高价:不复权","最低价:不复权", "收盘价:不复权","涨跌幅:前复权","成交量", "成交额","复权因子", "新股上市日期"]

Fields_swl = ["股票简称", "股票代码", "市盈率(pe)", "市净率(pb)", "所属申万行业",'所属同花顺行业']

Fields_new_high = ["股票简称", "股票代码", '最新价', '最新涨跌幅', "所属申万行业"]

Fields_basic = ["股票简称", "股票代码", "市盈率(pe)", "市净率(pb)", '总市值','a股市值(不含限售股)',"所属申万行业",'所属同花顺行业','所属概念']

Fields_return_query =  ["5日涨幅", "10日涨幅","20日涨幅","60日涨幅","120日涨幅","250日涨幅"]
Fields_ma_query =  ["5日均线", "10日均线","20日均线","60日均线","120日均线","250日均线"]

Fields_high_low_250 = ["250日最高价","250日最低价"]
Fields_high_low_history = ["历史最高价","历史最低价"]
Fields_high_period = ["历史最高价","250日最高价"]

Fields_query_daily = ["收盘价不复权","成交量", "复权因子"]

Fields_query_etf = ['etf']

Fields_query_condbond = ['可转债']

Fields_query_index = ['同花顺行业指数','三级行业']


class QUERY_TYPE():
    stock="stock"
    fund="fund"
    index="zhisu"
    bond="conbond"

class PERIODS():
    """stock trade period
    """
    PERIODS=[5,10,20,60,120,250]

class SWL_LEVEL():
    LEVEL =['L1','L2','L3']
    SWL_LEVEL = ['sw_l1','sw_l2','sw_l3']


class PERIODS_RETURN_CN():
    PERIODS_RETURN= ["5日涨幅", "10日涨幅","20日涨幅","60日涨幅","120日涨幅","250日涨幅"]



class PERIODS_LIST():
    NList = PERIODS().PERIODS
    RT_LIST = [f"rt{x}" for x in NList ]
    RS_LIST = [f"rs{x}" for x in NList ]


class Exchange(Enum):
    #: 上证交易所
    sh = "sh"
    #: 深证交易所
    sz = "sz"
    #: bj
    bj = "bj"

class SWL_LEVEL():
    LEVEL =['L1','L2','L3']
    SWL_LEVEL = ['sw_l1','sw_l2','sw_l3']

class PERIODS():
    """stock trade period
    """
    PERIODS=[5,10,20,60,120,250]

class REPORT_PERIODS():
    q1 = '0331'
    q2 = '0630'
    q3 = '0930'
    q4 = '1231'
    REPORT_PERIODS_DICT = { 'q1': '0331',
            'q2': '0630',
            'q3': '0930',
            'q4': '1231'}


class TRADE_TIMES():
    TRADE_TIME_AM = ['09:30:00','11:30:00']
    TRADE_TIME_PM = ["13:00:00","15:00:00"]
    TRADE_TIME_AM_pre = ['09:25:00','11:31:00']
    TRADE_TIME_PM_pre = ["13:00:00","15:01:00"]
