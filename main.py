from config.mysql_config import (
    get_db1_connection, 
    get_db2_connection, 
    get_db3_connection, 
    get_db4_connection, 
    get_db5_connection
)
from config.mongo_config import get_mongo_connection
from db.mysql_connector import fetch_mysql_data_vino12, fetch_mysql_data_vino34, fetch_mysql_data_vino5
from utils.data_unifier import unify_data
from utils.logger import setup_logger

def save_unified_data_to_mongo(connection, unified_data):
    db = connection["unificacion_vino"]  # Actualizado para reflejar la base de datos correcta
    collection = db["vino_unificados"]  # Actualizado para reflejar la colección correcta
    
    try:
        collection.insert_many(unified_data)
        print(f"{len(unified_data)} documentos insertados en MongoDB.")
    except Exception as e:
        print(f"Error al insertar los documentos en MongoDB: {e}")

def main():
    logger = setup_logger("output/logs.txt")

    # Conectar a las bases de datos MySQL
    conn_db1 = get_db1_connection()
    conn_db2 = get_db2_connection()
    conn_db3 = get_db3_connection()
    conn_db4 = get_db4_connection()
    conn_db5 = get_db5_connection()

    # Extraer datos de las tablas correspondientes
    mysql_data_vino12_db1 = fetch_mysql_data_vino12(conn_db1)
    mysql_data_vino12_db2 = fetch_mysql_data_vino12(conn_db2)
    mysql_data_vino34_db3 = fetch_mysql_data_vino34(conn_db3)
    mysql_data_vino34_db4 = fetch_mysql_data_vino34(conn_db4)
    mysql_data_vino5_db5 = fetch_mysql_data_vino5(conn_db5)

    # Unificar los datos
    unified_data_vino12 = mysql_data_vino12_db1 + mysql_data_vino12_db2
    unified_data_vino34 = mysql_data_vino34_db3 + mysql_data_vino34_db4

    unified_data = unify_data(unified_data_vino12, unified_data_vino34, mysql_data_vino5_db5)

    # Conectar a MongoDB y guardar los datos unificados
    mongo_conn = get_mongo_connection()
    save_unified_data_to_mongo(mongo_conn, unified_data)

    logger.info("Proceso de unificación completado y datos guardados exitosamente en MongoDB.")

if __name__ == "__main__":
    main()
