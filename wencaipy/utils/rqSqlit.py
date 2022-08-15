import sqlite3

def sqlite_operation():
    conn =  sqlite3.connect("/mnt/f/Stock/wencai/wencai.db")
    cur = conn.cursor()
    #cur.execute("PRAGMA foreign_keys = ON")

    cur.execute('''
        CREATE TABLE index_sw_class(
                index_code TEXT  PRIMARY KEY(index_code), 
                index TEXT,
                index_name TEXT, 
                level TEXT, 
                name_level TEXT,
                )
            ''')

    conn.commit()
    conn.close()


