import time
from wencaipy.stock import stock_prs

from wencaipy.common.dataToExcel import read_data_from_excel
from wencaipy.common.tradeDate import get_real_trade_date
from wencaipy.stock.stock_prs import stock_prs_oh_ol_volchg_inc_forecast_concept

def save_stock_prs_to_excel():
    #stock_prs.stock_prs_oh_ol_volchg_inc()
    #stock_prs.stock_prs_oh_ol_volchg_inc_concept()
    stock_prs_oh_ol_volchg_inc_forecast_concept()
    
    
if __name__ == "__main__":
    start_time = time.perf_counter()
    save_stock_prs_to_excel()
    end_time = time.perf_counter()
    times = end_time - start_time
    print(f"Tasted times: {times}s")