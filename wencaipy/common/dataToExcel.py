import os
import pandas as pd

from wencaipy.common.wcParameter import PATH_VPS_IWENCAI, SQLITE_PATH_RR_PC , PATH_ALIYUN_IWENCAI


def path(server_name="VPS"):
    if server_name == "ALIYUN":
        PATH  = PATH_ALIYUN_IWENCAI
    if server_name ==  "WSL":
        PATH = SQLITE_PATH_RR_PC
    if  server_name == "VPS":
        PATH = PATH_VPS_IWENCAI

    if not os.path.exists(PATH):
        os.makedirs(PATH)
    print(PATH)
    return PATH


def data_to_excel(data=None,file_name=None, server_name="VPS"):
    PATH = path(server_name=server_name)
    try:
        data.to_excel(f"{PATH}/{file_name}.xlsx")
        print(f"Save data to excel <{file_name}.xlsx> finish !")
    except Exception as e:
        print(e)


def read_data_from_excel(file_name=None, server_name="VPS"):
    PATH =  path(server_name=server_name)
    try:
        return pd.read_excel(f"{PATH}/{file_name}.xlsx",index_col=0)
        print(f"Read data from excel <{file_name}.xlsx> finish !")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print(path(server_name="VPS"))
    #print(read_data_from_excel("trade_date_sse"))
    #print(read_data_from_excel("stock_ma"))




