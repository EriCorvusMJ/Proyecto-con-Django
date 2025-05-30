import psycopg2

try:
    conn = psycopg2.connect(
        dbname="snake",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    print("Conexión exitosa")
    conn.close()
except Exception as e:
    print("Error al conectar:", e)
