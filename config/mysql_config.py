import pymysql

def get_mysql_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Antobriox10*',
        db='unificar_datos'
    )
