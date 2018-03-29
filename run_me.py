import sys

import zipcode


if __name__ == '__main__':
    assert len(sys.argv) == 3, 'Please specify two zipcodes to calculate distance between'
    zipcode_1 = sys.argv[1]
    zipcode_2 = sys.argv[2]
    latlong_cambridge = zipcode.get_lat_and_long(zipcode_1) 
    latlong_texas = zipcode.get_lat_and_long(zipcode_2) 
    print 'Distance between {zipcode_1} and {zipcode_2} is {distance} miles'.format(
        zipcode_1=zipcode_1,
        zipcode_2=zipcode_2,
        distance=zipcode.calculate_distance(latlong_cambridge, latlong_texas)
    )
