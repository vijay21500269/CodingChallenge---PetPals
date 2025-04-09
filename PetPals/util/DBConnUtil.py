import mysql.connector
from util.DBPropertyUtil import load_db_properties

def get_db_connection():
    config = load_db_properties()
    try:
        connection = mysql.connector.connect(
            host=config["host"],
            port=int(config["port"]),
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return connection
    except Exception as e:
        print("Error while establishing DB connection:", e)
        return None
