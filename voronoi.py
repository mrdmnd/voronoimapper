import sys
import pandas
import numpy as np

def main(stops_path, rides_path):
    with open(stops_path, 'rb') as stops_file, open(rides_path, 'rb') as rides_file:
        stops_tsv = pandas.read_csv(stops_file, delimiter='\t', header=None, names=["lat", "lng", "name"])
        rides_tsv = pandas.read_csv(rides_file, delimiter='\t', header=None, names=["lat_start", "lng_start", "lat_end", "lng_end", "id"])
        print stops_tsv
        print rides_tsv


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Requires a stops argument and a rides argument."
    stops_path = sys.argv[1]
    rides_path = sys.argv[2]
    main(stops_path, rides_path)
