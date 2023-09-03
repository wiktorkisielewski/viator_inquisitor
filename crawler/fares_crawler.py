import csv
from api import *
# from psql import *

airports_csv_file_path = 'airports.csv'

def get_main_airports():
    main_airports = []

    with open(airports_csv_file_path, 'r') as airports_csv:
        airports_data = csv.reader(airports_csv, delimiter=',')
        filtered_airports_data = [row for row in airports_data if row[13] and row[7] == 'EU' and (row[2] == 'large_airport' or row[2] == 'medium_airport')]
        for row in filtered_airports_data:
            main_airports.append([row[3], row[13]])
    
    return main_airports

def tommorow_connections():
    for airport in get_main_airports():
        tomorrow = datetime.today().date() + timedelta(days=1)
        tomorrow_1 = tomorrow + timedelta(days=1)
        destinations = get_destinations(origin=airport[1], date_from=tomorrow,date_to=tomorrow_1)

        if destinations != []:
            print(airport, destinations)

def safe_data(origin):
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {origin} (
        origin_airport TEXT,
        origin_iata_code TEXT,
        time TIMESTAMP,
        price FLOAT,
        currency TEXT
    );
    """

    cursor.execute(create_table_sql)
    connection.commit()    
