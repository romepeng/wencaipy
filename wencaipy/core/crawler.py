# -*- coding:utf-8 -*-
import logging
import re
import requests
import pandas as pd
from wencaipy.core.cons import WENCAI_CRAWLER_URL, WENCAI_HEADERS
from wencaipy.core.content import BackTest, YieldBackTest, EventBackTest, LastJs
from wencaipy.core.cookies import WencaiCookie
from wencaipy.core.session import Session
from wencaipy.common.wcParameter import (MAX_QUERY_SIZE, QUERY_TYPE,Question_Url,headers_wc,
                                         Drop_columns_ipo, Drop_columns_ipo_2, Fields_basic, Fields_query_etf, Fields_query_index)
from wencaipy.utils.tradeDate import today, if_traded_now, get_real_trade_date, get_last_tradedate

from wencaipy.common.wcParameter import Fields_query_condbond
from wencaipy.common.tradeDate import get_real_trade_date, if_traded_now, get_last_tradedate

class Wencai(object):
    logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s [%(levelname)s] %(message)s',
    )

    def __init__(self, cn_col=False, proxies=None, verify=False):
        self.cookies = WencaiCookie()
        self.cn_col = cn_col
        self.session = Session(proxies=proxies, verify=verify)

    def backtest(self, query, start_date, end_date, period, benchmark):
        payload = {
            "query": query,
            "start_date": start_date,
            "end_date": end_date,
            "period": period,
            "benchmark": benchmark
        }

        r = self.session.post_result(source='backtest', url=WENCAI_CRAWLER_URL['backtest'], data=payload)
        if r.status_code == 200:
            print(r.json())
            return BackTest(content=r.json(), cn_col=self.cn_col, start_date=start_date, end_date=end_date,
                            session=self.session)

        else:
            raise Exception(r.content.decode('utf-8'))

    def yieldbacktest(self, query, start_date, end_date, stock_hold, upper_income, lower_income, period, fall_income,
                      day_buy_stock_num):
        payload = {
            "query": query,
            "start_date": start_date,
            "end_date": end_date,
            "period": period,
            "stock_hold": stock_hold,
            "upper_income": upper_income,
            "lower_income": lower_income,
            "fall_income": fall_income,
            "day_buy_stock_num": day_buy_stock_num
        }
        r = self.session.post_result(WENCAI_CRAWLER_URL['yieldbacktest'], data=payload,
                                     add_headers=WENCAI_HEADERS['backtest'], source='backtest')
        if r.status_code == 200:
            return YieldBackTest(content=r.json(), cn_col=self.cn_col, query=query,
                                 start_date=start_date, end_date=end_date,
                                 session=self.session)
        else:
            raise Exception(r.content.decode('utf-8'))

    def eventbacktest(self, query, index_code, period, start_date, end_date):
        payload = {
            "query": query,
            "start_date": start_date,
            "end_date": end_date,
            "period": period,
            "index_code": index_code
        }

        r = self.session.post_result(WENCAI_CRAWLER_URL['eventbacktest'], data=payload, source='eventbacktest')
        if r.status_code == 200:
            return EventBackTest(content=r.json(), cn_col=self.cn_col)
        else:
            raise Exception(r.content.decode('utf-8'))

    def lastjs(self, code):
        r = self.session.get_result(WENCAI_CRAWLER_URL['lastjs'].format(code), source='lastjs',
                                    add_headers=WENCAI_HEADERS['lastjs'])
        if r.status_code == 200:
            return LastJs(content=r.text, code=code).get_data
        else:
            raise Exception(r.content.decode('utf-8'))

    def search(self, query_string): #TODO

        payload = {
            "question": query_string,
            "page": 1,
            "perpage": 100,
            "log_info": '{"input_type": "typewrite"}',
            "source": "Ths_iwencai_Xuangu",
            "version": 2.0,
            "secondary_intent": "",
            "query_area": "",
            "block_list": "",
            "add_info": '{"urp": {"scene": 1, "company": 1, "business": 1}, "contentType": "json", "searchInfo": true}'
        }

        r = self.session.post_result(url=WENCAI_CRAWLER_URL['search'],
                                     data=payload, force_cookies=True)
        result = r.json()['data']['answer'][0]['txt'][0]['content']['components'][0]['data']['datas']

        def _re_str(x: str):
            _re = re.findall('(.*):前复权', x)
            if len(_re) >= 1:
                x = _re[-1]
            check_date = re.search(r"(\d{4}\d{1,2}\d{1,2})",x)
            if check_date is not None:
                return x.replace('[{}]'.format(check_date.group()), '')
            else:
                return x

        data = pd.DataFrame().from_dict(result)
        if not data.empty:
            columns = {i: _re_str(i) for i in data.columns}
            data = data.rename(columns=columns)
            for col in ['market_code', 'code', '关键词资讯', '涨跌幅']:
                if col in data.columns:
                    del data[col]
        return data
    
    
    def search_data(self, trade_date=None, fields_query=None):
        if not trade_date:
            if if_traded_now():
                trade_date = today()
            else:
                trade_date= get_last_tradedate()
        trade_date = get_real_trade_date(trade_date)
        print(trade_date)
        
        payload = {
            # 查询问句
            "question": "{},{},上市日期<={}".format(trade_date, ",".join(fields_query), trade_date),
            # 返回查询记录总数 
            "perpage": MAX_QUERY_SIZE,
            "query_type": QUERY_TYPE.stock
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
                df = df_data 
              
                df = df.assign(trade_date = trade_date) #, code=df["股票代码"].apply(lambda x: x[0:6])).set_index("trade_date", drop=True)
                return df
            else:
                print(f"连接访问接口失败")           
        except Exception as e:
            print(e)

        
