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
    connection.autocommit = True

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         "SELECT version();"
    #     )
    #     print(f"Server version: {cursor.fetchone()}")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO notes(title, content, link, hash) VALUES
    #         ('Первая запись', 'Содержание первой записи', '//link', '# хеш');"""
    #     )
    #     print("[INFO] Data was succesfully inserted")

    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM notes"""
        )
        print(cursor.fetchone())

except Exception as er:
    print("[INFO] Error while working with PostgreSQL", er)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
