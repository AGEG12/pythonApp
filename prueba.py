import pymysql

conexion = pymysql.connect(
    host='bwhehcigjcjvxxnzgosa-mysql.services.clever-cloud.com',
    user='ug00sdj4gxqt9r09',
    password='Ie52j7fid7EtTrNlzyhc',
    database='bwhehcigjcjvxxnzgosa'
)
cursor = conexion.cursor()

try:
    # Obtener todos resultados de la tabla de productos
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    print("Usuarios:")
    for user in users:
        print(user)

except pymysql.MySQLError as e:
    print(f"Error en la conexión o consulta: {e}")
finally:
    cursor.close()
    conexion.close()