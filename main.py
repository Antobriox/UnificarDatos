from config.mysql_config import get_mysql_connection
from config.mongo_config import get_mongo_connection
from db.mysql_connector import fetch_mysql_data
from db.mongo_connector import fetch_mongo_data
from utils.data_unifier import unify_data
from utils.logger import setup_logger

def main():
    logger = setup_logger("output/logs.txt")

    # Conectar a las bases de datos
    mysql_conn = get_mysql_connection()
    mongo_conn = get_mongo_connection()

    # Extraer datos
    mysql_data = fetch_mysql_data(mysql_conn)
    mongo_data = fetch_mongo_data(mongo_conn)

    # Unificar datos
    unified_data = unify_data(mysql_data, mongo_data)

    # Guardar o procesar datos unificados
    # Aquí podrías guardar los datos unificados en una nueva base de datos
    # o realizar cualquier otra acción necesaria.

    logger.info("Proceso de unificación completado exitosamente.")

if __name__ == "__main__":
    main()
