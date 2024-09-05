import pymysql

def get_mysql_connection(db_name):
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Antobriox10*',
        db=db_name
    )

# Conexiones específicas para cada una de las 5 bases de datos
def get_db1_connection():
    return get_mysql_connection('db1')

def get_db2_connection():
    return get_mysql_connection('db2')

def get_db3_connection():
    return get_mysql_connection('db3')

def get_db4_connection():
    return get_mysql_connection('db4')

def get_db5_connection():
    return get_mysql_connection('db5')

# Conexión a la base de datos de unificación completa
def get_unificacion_completa_connection():
    return get_mysql_connection('unificacion_vino')
