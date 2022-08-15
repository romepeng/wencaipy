import pandas as pd
from pandas.io.sql import read_sql_table
import pymysql
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:Mysqlpd1219.@localhost/iwencai')

def create_mysqlDB(db_name="iwencai"):
    # Create a connection object
    databaseServerIP            = "127.0.0.1"  # IP address of the MySQL database server
    databaseUserName            = "root"       # User name of the database server
    databaseUserPassword        = "Mysqlpd1219."           # Password for the database user
    newDatabaseName             = db_name # Name of the database that is to be created
    charSet                     = "utf8mb4"     # Character set
    cusrorType                  = pymysql.cursors.DictCursor
    connectionInstance   = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
                                        charset=charSet,cursorclass=cusrorType)
    try:
        # Create a cursor object
        cursorInsatnce        = connectionInstance.cursor()
        # SQL Statement to create a database
        sqlStatement            =  f"CREATE DATABASE {newDatabaseName}"
        # Execute the create database SQL statment through the cursor instance
        cursorInsatnce.execute(sqlStatement)
        # SQL query string
        sqlQuery            = "SHOW DATABASES"
        # Execute the sqlQuery
        cursorInsatnce.execute(sqlQuery)
        #Fetch all the rows
        databaseList                = cursorInsatnce.fetchall()
        for datatbase in databaseList:
            print(datatbase)
    except Exception as e:
        print("Exeception occured:{}".format(e))
    finally:
        connectionInstance.close()


def saveToMysql(df, table_name, con=engine,chunksize=5000,if_exists='replace',index=None):
    df.to_sql(name=table_name, con=con, chunksize=chunksize,if_exists=if_exists, index=index)
    print(f'Save dataframe to mysqldb table <{table_name}>.')


def readFromMysql(table_name,con=engine):
    print(f'Read table from {table_name}')
    return pd.read_sql_table(table_name=table_name, con=con)


if __name__ == "__main__":
    create_mysqlDB(db_name='iwencai')
    from wencaipy.common.dataToExcel import read_data_from_excel
    df = read_data_from_excel("stock_prs_oh_volchg_inc_forecast_concept_2022-08-12")
    print(df)
    saveToMysql(df,'stock_prs')
    print(read_sql_table(table_name='stock_prs',con=engine))


