import psycopg2

from config import user, password, host, db_name, port

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE notes(
            id serial PRIMARY KEY,
            title varchar(50) NOT NULL,
            content varchar(1000) NOT NULL,
            link varchar(200) NOT NULL,
            hash varchar(200) NOT NULL);"""
        )
    print("[INFO] Table created succesfully")
except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
