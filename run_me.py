import csv
import sys

import zipcode


if __name__ == '__main__':
    assert len(sys.argv) == 2, 'Please specify filename'
    filename = sys.argv[1]

    # open new file for writing
    with open('zipcodes_with_distances.csv', 'w') as csv_output:
        fieldnames = ['zipcode1', 'zipcode2', 'distance (mi)']
        writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
        writer.writeheader()

        with open(filename) as csvfile_input:
            reader = csv.DictReader(csvfile_input)
            for row in reader:
                latlong_1 = zipcode.get_lat_and_long(row['zipcode1']) 
                latlong_2 = zipcode.get_lat_and_long(row['zipcode2']) 
                distance = zipcode.calculate_distance(latlong_1, latlong_2)
                writer.writerow({
                    'zipcode1': row['zipcode1'],
                    'zipcode2': row['zipcode2'],
                    'distance (mi)': distance
                })
    print 'New file created: zipcodes_with_distances.csv'
