from dataclasses import replace
from sqlalchemy import engine_from_config
from wencaipy.stock import stock_prs

from wencaipy.common.dataToExcel import read_data_from_excel
from wencaipy.common.operationSqlite import SQLITEDB
from wencaipy.common.tradeDate import get_real_trade_date
from wencaipy.stock.stock_prs import stock_prs_oh_ol_volchg_inc_forecast_concept
#from rrdata.common.engine_pgsql import engine
from rrshare.rqUtil import PgsqlClass


def save_stock_prs_to_sqlite(): #TODO
    #stock_prs.stock_prs_oh_ol_volchg_inc()
    #stock_prs.stock_prs_oh_ol_volchg_inc_concept()
    #df = stock_prs_oh_ol_volchg_inc_forecast_concept()
    df = read_data_from_excel("stock_prs_oh_volchg_inc_forecast_concept_2022-07-29")
    #con = SQLITEDB().sqlite_engine()
    print(df.head())
    #df.to_sql('stock_prs_wencai', con=engine())
    PgsqlClass().insert_to_psql(df, 'rrshare','stock_prs_iwencai',if_exists='replace')

  
    
if __name__ == "__main__":
    save_stock_prs_to_sqlite()