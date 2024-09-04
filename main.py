from config.mysql_config import get_mysql_connection, get_unificacion_completa_connection
from config.mongo_config import get_mongo_connection
from db.mysql_connector import fetch_mysql_data
from db.mongo_connector import fetch_mongo_data
from utils.data_unifier import unify_data
from utils.logger import setup_logger

def save_unified_data_to_db(connection, unified_data):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO datos_unificados (nombre, apellido, cedula, fecha_nacimiento, direccion, numero_telefono)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    for data in unified_data:
        cursor.execute(insert_query, (
            data['nombre'],
            data['apellido'],
            data['cedula'],
            data['fecha_nacimiento'],
            data['direccion'],
            data['numero_telefono']
        ))
    
    connection.commit()
    cursor.close()

def main():
    logger = setup_logger("output/logs.txt")

    # Conectar a las bases de datos
    mysql_conn = get_mysql_connection()
    mongo_conn = get_mongo_connection()
    unificacion_completa_conn = get_unificacion_completa_connection()

    # Extraer datos
    mysql_data = fetch_mysql_data(mysql_conn)
    mongo_data = fetch_mongo_data(mongo_conn)

    # Unificar datos
    unified_data = unify_data(mysql_data, mongo_data)

    # Guardar datos unificados en la nueva base de datos
    save_unified_data_to_db(unificacion_completa_conn, unified_data)

    logger.info("Proceso de unificación completado y datos guardados exitosamente.")

if __name__ == "__main__":
    main()
