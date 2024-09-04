def fetch_mysql_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT nombre, apellido, cedula FROM personas")
    data = cursor.fetchall()
    connection.close()
    return data
  