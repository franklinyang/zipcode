# https://pypi.python.org/pypi/pyzipcode

from geopy import distance
from pyzipcode import ZipCodeDatabase


def calculate_distance(lat_long_1, lat_long_2):
    return distance.vincenty(lat_long_1, lat_long_2).miles


def get_lat_and_long(zipcode):
    zcdb = ZipCodeDatabase()
    zipcode_details = zcdb[zipcode]
    latitude, longitude = (zipcode_details.latitude, zipcode_details.longitude)
    return (latitude, longitude)
