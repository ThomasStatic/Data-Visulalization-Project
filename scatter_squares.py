import matplotlib.pyplot as mplplt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

mplplt.style.use('seaborn')
fig,ax = mplplt.subplots()

# c controls colour, s controls point size, cmap controls colour map
ax.scatter(x_values,y_values, c = y_values, cmap = mplplt.cm.Blues, s = 10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Square of Values", fontsize = 14)

# Set size of tick labels (note, which = 'major' indicates we are talking about the major ticks)
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

# Set the range for each axis
ax.axis([0,1100,0,1_100_000])

# bbox_inches = 'tight' trims off extra whitespace from the saved file
mplplt.savefig("squares_plot.png", bbox_inches = 'tight')