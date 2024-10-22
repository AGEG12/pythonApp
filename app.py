import os
import pymysql

def connect_to_db():
    connection = pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return connection

def fetch_users():
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            results = cursor.fetchall()
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    finally:
        connection.close()

# Llamada a la función para obtener datos de los usuarios
if __name__ == "__main__":
    fetch_users()