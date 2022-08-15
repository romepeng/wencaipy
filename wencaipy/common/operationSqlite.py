from http import server
from importlib.resources import path
import sqlite3
from sqlalchemy import create_engine

from wencaipy.common.wcParameter import PATH_WSL_IWENCAI ,PATH_ALIYUN_IWENCAI, PATH_VPS_IWENCAI

print(PATH_WSL_IWENCAI ,PATH_ALIYUN_IWENCAI, PATH_VPS_IWENCAI)

class SQLITEDB(object):

    def __init__(self, server_name="SWL", db_name=""):
        self.server_name = server_name
        if not db_name:
            self.db_name ="iwencai.db"
        else:
            self.db_name= f"{db_name}.db"

        
    def path(self):
        if self.server_name == "WSL": 
            path =  PATH_WSL_IWENCAI
        if self.server_name == "ALIYUN": 
            path = PATH_ALIYUN_IWENCAI
        if self.server_name == "VPS" : 
            spath = PATH_VPS_IWENCAI
        return path
        
        
    def sqlite_engine(self):
        file_path = f"{self.path}{self.db_name}"
        print(file_path)
        return create_engine(f"sqlite:////{self.path}{self.db_name}") #,execution_options={"sqlite_raw_colnames":True})
      

    def sqlite_create_table(self,table_cols = "tarde_date,sec_code,sec_name,close, pct_chg, thsl,concept",
                        table_name="basic"):  # ALIYUN or VPS
        print(self.path)
        conn = sqlite3.connect(f"{self.path}{self.db_name}")   
        cur = conn.cursor()
        #cur.execute("PRAGMA foreign_keys = ON")
        cols = table_cols
        sql = f"CREATE TABLE IF NOT EXISTS {table_name}({cols})"
        cur.execute(sql)
        conn.commit()
        print(f"Create sqlite database <{self.db_name}> table <{table_name}>  finish!")
        conn.close()
    
if __name__ == "__main__":
    sql = SQLITEDB(server_name="WSL")
    sql.sqlite_engine()
    sql.sqlite_create_table()
    
    
    