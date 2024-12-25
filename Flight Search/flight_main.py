import time
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight


flight_search = FlightSearch()

# Set your origin airport
ORIGIN_CITY_IATA = "IST"
DEST_CITY_IATA = "BUD"


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


flights = flight_search.check_flights(
    ORIGIN_CITY_IATA,
    DEST_CITY_IATA,
    from_time=tomorrow,
    to_time=six_month_from_today
)

cheapest_flight = find_cheapest_flight(flights)
print(f"{DEST_CITY_IATA}: £{cheapest_flight.price}")
print(cheapest_flight.origin_airport, cheapest_flight.destination_airport, cheapest_flight.out_date,cheapest_flight.return_date)
time.sleep(2)
