"""
这里定义的是一些常用常量
"""
from enum import Enum
from pytz import timezone

CHINA_TZ = timezone("Asia/Shanghai")

startDate = "2020-04-28"  #rq_util_get_pre_trade_date(rq_util_get_last_tradedate(), 255)

MAX_QUERY_SIZE: int = 5000
TS_DATE_FORMATE: str = '%Y%m%d'
MAX_QUERY_TIMES: int = 500

SQLITE_PATH_RR_PC = "/mnt/f/Stock/iwencai/"
SQLITE_PATH_ALIYUN = "/mnt/disk1/sqlit_data"


class AdjustType(Enum):
    """
    split-adjusted type for :class:`~.zvt.contract.schema.TradableEntity` quotes
    """
    #: not adjusted
    #: 不复权
    bfq = "bfq"
    #: pre adjusted
    #: 不复权
    qfq = "qfq"
    #: post adjusted
    #: 不复权
    hfq = "hfq"


class ActorType(Enum):
    #: 个人
    individual = "individual"
    #: 公募基金
    raised_fund = "raised_fund"
    #: 社保
    social_security = "social_security"
    #: 保险
    insurance = "insurance"
    #: 外资
    qfii = "qfii"
    #: 信托
    trust = "trust"
    #: 券商
    broker = "broker"
    #: 私募
    private_equity = "private_equity"
    #: 公司(可能包括私募)
    corporation = "corporation"


class Exchange(Enum):
    #: 上证交易所
    sh = "sh"
    #: 深证交易所
    sz = "sz"
    #: bj
    bj = "bj"



class TRADE_TIMES():
    TRADE_TIME_AM = ['09:30:00','11:30:00']
    TRADE_TIME_PM = ["13:00:00","15:00:00"]
    TRADE_TIME_AM_pre = ['09:25:00','11:31:00']
    TRADE_TIME_PM_pre = ["13:00:00","15:01:00"]

#print(TRADE_TIMES().TRADE_TIME_AM)

class REPORT_PERIODS():
    q1 = '0331'
    q2 = '0630'
    q3 = '0930'
    q4 = '1231'
    REPORT_PERIODS_DICT = { 'q1': '0331',
            'q2': '0630',
            'q3': '0930',
            'q4': '1231'}
    
class PERIODS():
    """stock trade period
    """
    PERIODS=[5,10,20,60,120,250]

class SWL_LEVEL():
    LEVEL =['L1','L2','L3']
    SWL_LEVEL = ['sw_l1','sw_l2','sw_l3']



class EXCHANGE_ID():
    SSE = 'sse'  # 上交所
    SZSE = 'szse'  # 深交所
    BSE = 'bse' # 北京交易所
    SHFE = 'SHFE'  # 上期所
    DCE = 'DCE'  # 大商所
    CZCE = 'CZCE'  # 郑商所
    CFFEX = 'CFFEX'  # 中金所
    INE = 'INE'  # 能源中心
    HUOBI = 'huobi' # 火币Pro
    BINANCE = 'binance' # 币安
    BITMEX = 'bitmex' # BITMEX
    BITFINEX = 'BITFINEX' # BITFINEX
    OKEX = 'OKEx' # OKEx



class MARKET_TYPE():
    """市场种类
    日线 尾数01
    分钟线 尾数02
    tick 尾数03
    市场:
    股票 0
    指数/基金 1
    期货 2
    港股 3
    美股 4
    比特币/加密货币市场 5
    """
    STOCK_CN = 'stock_cn'  # 中国A股
    STOCK_CN_B = 'stock_cn_b'  # 中国B股
    STOCK_CN_D = 'stock_cn_d'  # 中国D股 沪伦通
    STOCK_HK = 'stock_hk'  # 港股
    STOCK_US = 'stock_us'  # 美股
    FUTURE_CN = 'future_cn'  # 国内期货
    OPTION_CN = 'option_cn'  # 国内期权
    STOCKOPTION_CN = 'stockoption_cn'  # 个股期权
    # BITCOIN = 'bitcoin'  # 比特币
    CRYPTOCURRENCY = 'cryptocurrency'  # 加密货币(衍生货币)
    INDEX_CN = 'index_cn'  # 中国指数
    FUND_CN = 'fund_cn'   # 中国基金
    BOND_CN = 'bond_cn'  # 中国债券



class CURRENCY_TYPE():
    """货币种类"""
    RMB = 'rmb'  # 人民币
    USD = 'usd'  # 美元
    EUR = 'eur'  # 欧元
    HKD = 'hkd'  # 港币
    GBP = 'GBP'  # 英镑
    BTC = 'btc'  # 比特币
    JPY = 'jpy'  # 日元
    AUD = 'aud'  # 澳元
    CAD = 'cad'  # 加拿大元


class DATASOURCE():
    """数据来源
    """

    WIND = 'wind'  # wind金融终端
    TDB = 'tdb'  # wind tdb
    THS = 'ths'  # 同花顺网页
    TUSHARE = 'tushare'  # tushare
    TDX = 'tdx'  # 通达信
    MONGO = 'mongo'  # 本地/远程Mongodb
    PGSQL = 'postgresql' # 本地/远程Mongodb
    EASTMONEY = 'eastmoney'  # 东方财富网
    CHOICE = 'choice'  # choice金融终端
    CCXT = 'ccxt'  # github/ccxt 虚拟货币
    LOCALFILE = 'localfile'  # 本地文件
    AUTO = 'auto'  # 优先从Mongodb中读取数据，不足的数据从tdx下载


class OUTPUT_FORMAT():
    """输出格式
    """

    DATASTRUCT = 'datastruct'
    DATAFRAME = 'dataframe'
    SERIES = 'series'
    NDARRAY = 'ndarray'
    LIST = 'list'
    JSON = 'json'


class RUNNING_STATUS():
    """运行状态
    starting 是一个占用状态
    100 - 202 - 200 - 400 - 500
    """

    PENDING = 100
    SUCCESS = 200
    STARTING = 202
    RUNNING = 300
    WRONG = 400
    STOPED = 500
    DROPED = 600

class FREQUENCE():
    """查询的级别
    YEAR = 'year'  # 年bar
    QUARTER = 'quarter'  # 季度bar
    MONTH = 'month'  # 月bar
    WEEK = 'week'  # 周bar
    DAY = 'day'  # 日bar
    ONE_MIN = '1min'  # 1min bar
    FIVE_MIN = '5min'  # 5min bar
    FIFTEEN_MIN = '15min'  # 15min bar
    THIRTY_MIN = '30min'  # 30min bar
    HOUR = '60min'  # 60min bar
    SIXTY_MIN = '60min'  # 60min bar
    TICK = 'tick'  # transaction
    ASKBID = 'askbid'  # 上下五档/一档
    REALTIME_MIN = 'realtime_min' # 实时分钟线
    LATEST = 'latest'  # 当前bar/latest
    2019/08/06 @yutiansut
    """

    YEAR = 'year'  # 年bar
    QUARTER = 'quarter'  # 季度bar
    MONTH = 'month'  # 月bar
    WEEK = 'week'  # 周bar
    DAY = 'day'  # 日bar
    ONE_MIN = '1min'  # 1min bar
    FIVE_MIN = '5min'  # 5min bar
    FIFTEEN_MIN = '15min'  # 15min bar
    THIRTY_MIN = '30min'  # 30min bar
    HOUR = '60min'  # 60min bar
    SIXTY_MIN = '60min'  # 60min bar
    TICK = 'tick'  # transaction
    ASKBID = 'askbid'  # 上下五档/一档
    REALTIME_MIN = 'realtime_min'  # 实时分钟线
    LATEST = 'latest'  # 当前bar/latest

DATABASE_TABLE = {
    (MARKET_TYPE.STOCK_CN, FREQUENCE.DAY): 'stock_day',
    (MARKET_TYPE.STOCK_CN, FREQUENCE.ONE_MIN): 'stock_min',
    (MARKET_TYPE.STOCK_CN, FREQUENCE.FIVE_MIN): 'stock_min',
    (MARKET_TYPE.STOCK_CN, FREQUENCE.FIFTEEN_MIN): 'stock_min',
    (MARKET_TYPE.STOCK_CN, FREQUENCE.THIRTY_MIN): 'stock_min',
    (MARKET_TYPE.STOCK_CN, FREQUENCE.SIXTY_MIN): 'stock_min',
    (MARKET_TYPE.STOCK_CN, FREQUENCE.HOUR): 'stock_min',
    (MARKET_TYPE.STOCK_CN, FREQUENCE.TICK): 'stock_transaction',
    (MARKET_TYPE.INDEX_CN, FREQUENCE.DAY): 'index_day',
    (MARKET_TYPE.INDEX_CN, FREQUENCE.ONE_MIN): 'index_min',
    (MARKET_TYPE.INDEX_CN, FREQUENCE.FIVE_MIN): 'index_min',
    (MARKET_TYPE.INDEX_CN, FREQUENCE.FIFTEEN_MIN): 'index_min',
    (MARKET_TYPE.INDEX_CN, FREQUENCE.THIRTY_MIN): 'index_min',
    (MARKET_TYPE.INDEX_CN, FREQUENCE.SIXTY_MIN): 'index_min',
    (MARKET_TYPE.INDEX_CN, FREQUENCE.HOUR): 'index_min',
    (MARKET_TYPE.INDEX_CN, FREQUENCE.TICK): 'index_transaction',
    (MARKET_TYPE.FUND_CN, FREQUENCE.DAY): 'index_day',
    (MARKET_TYPE.FUND_CN, FREQUENCE.ONE_MIN): 'index_min',
    (MARKET_TYPE.FUND_CN, FREQUENCE.FIVE_MIN): 'index_min',
    (MARKET_TYPE.FUND_CN, FREQUENCE.FIFTEEN_MIN): 'index_min',
    (MARKET_TYPE.FUND_CN, FREQUENCE.THIRTY_MIN): 'index_min',
    (MARKET_TYPE.FUND_CN, FREQUENCE.SIXTY_MIN): 'index_min',
    (MARKET_TYPE.FUND_CN, FREQUENCE.HOUR): 'index_min',
    (MARKET_TYPE.FUND_CN, FREQUENCE.TICK): 'index_transaction',
    
}


class IntervalLevel(Enum):
    """
    Repeated fixed time interval, e.g, 5m, 1d.
    """

    #: level tick
    LEVEL_TICK = "tick"
    #: 1 minute
    LEVEL_1MIN = "1m"
    #: 5 minutes
    LEVEL_5MIN = "5m"
    #: 15 minutes
    LEVEL_15MIN = "15m"
    #: 30 minutes
    LEVEL_30MIN = "30m"
    #: 1 hour
    LEVEL_1HOUR = "1h"
    #: 4 hours
    LEVEL_4HOUR = "4h"
    #: 1 day
    LEVEL_1DAY = "1d"
    #: 1 week
    LEVEL_1WEEK = "1wk"
    #: 1 month
    LEVEL_1MON = "1mon"

    def to_pd_freq(self):
        if self == IntervalLevel.LEVEL_1MIN:
            return "1min"
        if self == IntervalLevel.LEVEL_5MIN:
            return "5min"
        if self == IntervalLevel.LEVEL_15MIN:
            return "15min"
        if self == IntervalLevel.LEVEL_30MIN:
            return "30min"
        if self == IntervalLevel.LEVEL_1HOUR:
            return "1H"
        if self == IntervalLevel.LEVEL_4HOUR:
            return "4H"
        if self >= IntervalLevel.LEVEL_1DAY:
            return "1D"

    def floor_timestamp(self, pd_timestamp):
        if self == IntervalLevel.LEVEL_1MIN:
            return pd_timestamp.floor("1min")
        if self == IntervalLevel.LEVEL_5MIN:
            return pd_timestamp.floor("5min")
        if self == IntervalLevel.LEVEL_15MIN:
            return pd_timestamp.floor("15min")
        if self == IntervalLevel.LEVEL_30MIN:
            return pd_timestamp.floor("30min")
        if self == IntervalLevel.LEVEL_1HOUR:
            return pd_timestamp.floor("1h")
        if self == IntervalLevel.LEVEL_4HOUR:
            return pd_timestamp.floor("4h")
        if self == IntervalLevel.LEVEL_1DAY:
            return pd_timestamp.floor("1d")

    def to_minute(self):
        return int(self.to_second() / 60)

    def to_second(self):
        return int(self.to_ms() / 1000)

    def to_ms(self):
        """
        To seconds count in the interval
        :return: seconds count in the interval
        """
        #: we treat tick intervals is 5s, you could change it
        if self == IntervalLevel.LEVEL_TICK:
            return 5 * 1000
        if self == IntervalLevel.LEVEL_1MIN:
            return 60 * 1000
        if self == IntervalLevel.LEVEL_5MIN:
            return 5 * 60 * 1000
        if self == IntervalLevel.LEVEL_15MIN:
            return 15 * 60 * 1000
        if self == IntervalLevel.LEVEL_30MIN:
            return 30 * 60 * 1000
        if self == IntervalLevel.LEVEL_1HOUR:
            return 60 * 60 * 1000
        if self == IntervalLevel.LEVEL_4HOUR:
            return 4 * 60 * 60 * 1000
        if self == IntervalLevel.LEVEL_1DAY:
            return 24 * 60 * 60 * 1000
        if self == IntervalLevel.LEVEL_1WEEK:
            return 7 * 24 * 60 * 60 * 1000
        if self == IntervalLevel.LEVEL_1MON:
            return 31 * 7 * 24 * 60 * 60 * 1000

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.to_ms() >= other.to_ms()
        return NotImplemented

    def __gt__(self, other):

        if self.__class__ is other.__class__:
            return self.to_ms() > other.to_ms()
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.to_ms() <= other.to_ms()
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.to_ms() < other.to_ms()
        return NotImplemented


class BlockCategory(Enum):
    #: 行业版块
    industry = "industry"
    #: 概念版块
    concept = "concept"
    #: 区域版块
    area = "area"


class IndexCategory(Enum):
    scope = "scope"
    #: 行业指数
    industry = "industry"
    #: 风格指数
    style = "style"
    #: fund
    fund = "fund"
   


class ReportPeriod(Enum):
    # 有些基金的2，4季报只有10大持仓，半年报和年报有详细持仓，需要区别对待
    season1 = "season1"
    season2 = "season2"
    season3 = "season3"
    season4 = "season4"
    half_year = "half_year"
    year = "year"
