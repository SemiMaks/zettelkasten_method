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

    with connection.cursor() as cursor:
