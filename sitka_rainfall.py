import csv
from datetime import datetime

import matplotlib.pyplot as mplplt

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get date and precipitation from file
	dates, precipitations = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		precipitation = row[3]
		dates.append(current_date)
		precipitations.append(precipitation)

# Plot the temperature
mplplt.style.use("seaborn")
fig,ax = mplplt.subplots()
ax.plot(dates, precipitations, c = 'blue')

ax.set_title("Daily precipitations - Sitka 2018", fontsize = 24)
ax.set_xlabel("", fontsize = 14)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation", fontsize = 14)
ax.tick_params(axis = 'both', which = 'major', labelsize = 4)

mplplt.show()
