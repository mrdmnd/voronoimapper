import sys
import pandas
import numpy as np
from sklearn.neighbors import KDTree

def main(stops_path, rides_path):
    with open(stops_path, 'rb') as stops_file, open(rides_path, 'rb') as rides_file:
        stops_df = pandas.read_csv(stops_file, delimiter='\t', header=None, names=["lat", "lng", "name"])
        rides_df = pandas.read_csv(rides_file, delimiter='\t', header=None, names=["lat_start", "lng_start", "lat_end", "lng_end", "ride_id"])

        stops_tree = KDTree(stops_df.as_matrix(columns=stops_df.columns[0:2]))
        rides_initial_points_array = rides_df.as_matrix(columns=rides_df.columns[0:2])
        rides_final_points_array = rides_df.as_matrix(columns=rides_df.columns[2:4])

        closest_initial_stop_array = stops_tree.query(rides_initial_points_array, return_distance=False)
        closest_final_stop_array = stops_tree.query(rides_final_points_array, return_distance=False)

        rides_df['index_initial_stop'] = closest_initial_stop_array
        rides_df['index_final_stop'] = closest_final_stop_array
        rides_df['closest_initial_stop'] = rides_df.index_initial_stop.map(stops_df.name)
        rides_df['closest_final_stop'] = rides_df.index_final_stop.map(stops_df.name)

        output_df = rides_df[["ride_id", "closest_initial_stop", "closest_final_stop"]]
        output_df.to_csv('output.tsv', sep='\t', index=False)



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Requires a stops argument and a rides argument."
    stops_path = sys.argv[1]
    rides_path = sys.argv[2]
    main(stops_path, rides_path)
