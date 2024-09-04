def fetch_mongo_data(connection):
    db = connection["unificar_datos"]
    collection = db["informacion_personal"]
    data = list(collection.find({}, {"_id": 0, "fecha_nacimiento": 1, "direccion": 1, "numero_telefono": 1}))
    return data
