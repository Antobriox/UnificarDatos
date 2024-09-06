def fetch_mysql_data_vino12(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT nombre_vino, color FROM vino12")
    data = cursor.fetchall()
    connection.close()
    return data

def fetch_mysql_data_vino34(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT porcentaje_alchol, año FROM vino34")
    data = cursor.fetchall()
    connection.close()
    return data

def fetch_mysql_data_vino5(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT nombre_vino, porcentaje_alchol FROM vino5")
    data = cursor.fetchall()
    connection.close()
    return data
