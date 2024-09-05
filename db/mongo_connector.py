def fetch_mongo_data(connection):
    db = connection["unificacion_vino"]  # Actualiza al nombre correcto de la base de datos
    collection = db["vino_unificados"]  # Actualiza al nombre correcto de la colección
    data = list(collection.find({}, {"_id": 0, "nombre_vino": 1, "color": 1, "porcentaje_alchol": 1, "ano": 1}))
    return data
