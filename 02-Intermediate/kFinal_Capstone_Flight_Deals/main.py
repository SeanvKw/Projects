from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint
# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

sheet_data = DataManager().get_data()
pprint(sheet_data)
