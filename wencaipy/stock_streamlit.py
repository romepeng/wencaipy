import streamlit as st

from wencaipy.common.rqMysql import readFromMysql
from wencaipy.stock.stock_prs import stock_prs_oh_ol_volchg_inc_forecast_concept


def stock_streamlit():
    df = readFromMysql('stock_prs')
    st.write(df)

if __name__ == "__main__":
    stock_streamlit()
