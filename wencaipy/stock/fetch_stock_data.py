from attr import field
from wencaipy.common.fetch_base_wencai import fetch_data_from_wencai
from wencaipy.common.dataToExcel import data_to_excel
from wencaipy.common.wcParameter import QUERY_TYPE


def fetch_stock_new_high(trade_date=None, new_high_period=0):
    """   股价创历史新高 new high; history=0 / 250 """
    if new_high_period == 0:
        Fields_new_high_query = ["股价创历史新高", "所属申万行业","所属同花顺行业"] 
    else:
        Fields_new_high_query = [f"{trade_date}日股票最高价创{new_high_period}日新高"]
    print(Fields_new_high_query)
    Fields_new_high = ["股票简称", "股票代码", '最新价', '最新涨跌幅', "所属申万行业","所属同花顺行业"]
    df = fetch_data_from_wencai(trade_date=trade_date,fields_query=Fields_new_high_query, fields_out=Fields_new_high, query_type=QUERY_TYPE.stock)
    data_to_excel(df, 'stock_new_high')
    return df


def fetch_stock_hot_sort():
    """ 个股热度排名"""
    df =  fetch_data_from_wencai(fields_query=["个股热度排名"], query_type=QUERY_TYPE.stock ).sort_values(by="个股热度排名")
    data_to_excel(df,'stock_hot')
    return df

def stock_super_strong():
    """ atr值/14日均价*现价；20天上涨天数；15日均线向上；5日均线在25日上， 10日均线在25日上;业绩涨幅大于50%或者业绩预告净利润大于50%；
    """
    Fields_super_strong = ['atr值/14日均价','15日均线向上',"概念",'同花顺三级行业'] #,"最新季度收入增幅大于50%","最新季度净利润增幅大于50%"]
    #["atr值/14日均价*现价","20天上涨天数",
       #,"15日均线向上 和 5日均线在25日上 和 10日均线在25日上",
                          #"业绩涨幅大于50%或者"
                         
    df = fetch_data_from_wencai(fields_query=Fields_super_strong, query_type=QUERY_TYPE.stock)
    data_to_excel(df,'stock_super')
    return df


def WCAlpha(object):
    """  """
    def __init_(self):
        self.get_datd_wencai = fetch_data_from_wencai()
        
    def ATR(self):
        pass
    
    def BOLL(self):
        pass
    
    def UPPCT():
        pass
    
        

if __name__ == "__main__":
    
    #print(fetch_stock_new_high())
    #print(fetch_stock_hot_sort()) 
    print(stock_super_strong())   
    
