import re
import pandas as pd

from dataToExcel import read_data_from_excel
from wencaipy.common.tradeDate import get_real_trade_date


df = read_data_from_excel(f"stock_prs_oh_volchg_inc_forecast_concept_{get_real_trade_date()}")
df.to_html("stock_prs.html",header=True, index=False)