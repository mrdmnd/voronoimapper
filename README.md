A program that takes two input files (`stops.tsv` and `rides.tsv`) and
returns a mapping from each ride to its corresponding closest stop.

First input models a collection of bus stop: `stops.tsv`

    Stop Latitude | Stop Longitude | Stop Name

Second input models a collection of transit rides: `rides.tsv`

    Initial Latitude | Inititial Longitude | Final Latitude | Final Longitude | Ride ID

Output is a file of the form `output.tsv`

    Ride ID | Closest Initial Stop | Closest Final Stop

Usage - Generate file `output.tsv` in current working directory:

    python voronoi.py `stops.tsv` `rides.tsv`

