import psycopg3
import os

# Define the database connection parameters
db_params = {
    'dbname': 'viator',
    'user': os.environ.get('PSQL_USERNAME'),
    'password': os.environ.get('PSQL_PASSWORD'),
    'host': os.environ.get('PSQL_HOST'),
    'port': os.environ.get('PSQL_PORT')
}

try:
    connection = psycopg3.connect(**db_params)
    cursor = connection.cursor()

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS fares (
        origin_airport TEXT,
        origin_iata_code TEXT,
        time TIMESTAMP,
        price FLOAT,
        currency TEXT
    );
    """

    cursor.execute(create_table_sql)
    connection.commit()

    cursor.close()
    connection.close()

except psycopg3.Error as e:
    print("Error connecting to the database:", e)
