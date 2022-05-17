import csv
from datetime import datetime

import matplotlib.pyplot as mplplt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)