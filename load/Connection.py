import pymysql

def connection():
    try:
        connection_db = pymysql.connect(host="localhost", user="root", passwd='', database="GoogleCloud")
        cursor = connection_db.cursor()
        return connection_db, cursor
    except Exception as error:
        cursor = ""
        connection_db = ""
        print(error)
        return connection_db, cursor