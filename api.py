from datetime import datetime, timedelta
from ryanair import Ryanair

api = Ryanair(currency="PLN")  # Euro currency, so could also be GBP etc. also
tomorrow = datetime.today().date() + timedelta(days=1)
tomorrow_1 = tomorrow + timedelta(days=10)

origin = input('origin: ')

flight = api.get_cheapest_flights(
        airport = str(origin),
        date_from = tomorrow,
        date_to = tomorrow,
        # destination_country = Optional[str] = None,
        departure_time_from = "00:00",
        departure_time_to = "23:59"
        # max_price = Optional[int] = None,
        # destination_airport = 'GLA'
    )

for i in flight:
    print(i[2], i[7])

# print(flight)