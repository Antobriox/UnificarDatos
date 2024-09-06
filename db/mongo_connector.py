def fetch_mongo_data(connection):
    db = connection["unificacion_vino"]  
    collection = db["vino_unificados"]  
    data = list(collection.find({}, {"_id": 0, "nombre_vino": 1, "color": 1, "porcentaje_alchol": 1, "año": 1}))
    return data
