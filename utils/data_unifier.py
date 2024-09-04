def unify_data(mysql_data, mongo_data):
    unified_data = []
    for mysql_row in mysql_data:
        for mongo_row in mongo_data:
            # Aquí accedemos a la cédula que está en la posición 2 de la tupla de MySQL
            if mysql_row['cedula'] == mongo_row["numero_telefono"]:
                unified_data.append({
                    "nombre": mysql_row['nombre'],  # Accediendo por nombre de columna
                    "apellido": mysql_row['apellido'],  # Accediendo por nombre de columna
                    "cedula": mysql_row['cedula'],  # Accediendo por nombre de columna
                    "fecha_nacimiento": mongo_row["fecha_nacimiento"],  # Clave corregida
                    "direccion": mongo_row["direccion"],
                    "numero_telefono": mongo_row["numero_telefono"]  # Clave corregida
                })
    return unified_data
