def unify_data(mysql_data, mongo_data):
    unified_data = []
    for mysql_row in mysql_data:
        for mongo_row in mongo_data:
            # Aquí accedemos a la cédula que está en la posición 2 de la tupla de MySQL
            if mysql_row[2] == mongo_row["numero_telefono"]:  # Índice 2 para la cédula
                unified_data.append({
                    "nombre": mysql_row[0],  # Índice 0 para el nombre
                    "apellido": mysql_row[1],  # Índice 1 para el apellido
                    "cedula": mysql_row[2],  # Índice 2 para la cédula
                    "fecha_nacimiento": mongo_row["fecha_nacimiento"],  # Clave corregida
                    "direccion": mongo_row["direccion"],
                    "numero_telefono": mongo_row["numero_telefono"]  # Clave corregida
                })
    return unified_data
