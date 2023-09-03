from datetime import datetime, timedelta
from ryanair import Ryanair

api = Ryanair(currency="PLN")  # Euro currency, so could also be GBP etc. also
tomorrow = datetime.today().date() + timedelta(days=1)
tomorrow_10 = tomorrow + timedelta(days=10)

def get_destinations(origin, date_from, date_to):
    destinations = []

    data = api.get_cheapest_flights(
            airport = str(origin),
            date_from = tomorrow,
            date_to = tomorrow,
            # destination_country = Optional[str] = None,
            departure_time_from = "00:00",
            departure_time_to = "23:59"
            # max_price = Optional[int] = None,
            # destination_airport = 'GLA'
        )

    for row in data:
        destination = [row[7], row[6]]
        destinations.append(destination)

    return destinations

# origin = input('origin: ')

# print('\npossible destitations: ')

# for d in get_destinations(origin=origin, date_from=tomorrow, date_to=tomorrow_10):
#     print(d)

# destination = input('\nenter destination airport code: ')

# flight = api.get_cheapest_flights(
#             airport = str(origin),
#             date_from = tomorrow,
#             date_to = tomorrow,
#             # destination_country = Optional[str] = None,
#             departure_time_from = "00:00",
#             departure_time_to = "23:59",
#             # max_price = Optional[int] = None,
#             destination_airport = str(destination)
#         )

# print(flight[0][1], flight[0][0], flight[0][2])