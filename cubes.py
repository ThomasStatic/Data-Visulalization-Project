import matplotlib.pyplot as mplplt

# Generate data of cubes
x_values = range(1,5001)
y_values = [x**2 for x in x_values]

# Set plot theme and generate plot variables
mplplt.style.use('seaborn')
fig,ax = mplplt.subplots()

# Plot the data on the graph
ax.scatter(x_values, y_values, c = y_values, cmap = mplplt.cm.Reds, s = 10)

ax.set_title("Cube Values", fontsize = 24)
ax.set_ylabel("Cube of Values", fontsize = 14)
ax.set_xlabel("Values", fontsize = 14)

ax.tick_params(axis = "both", labelsize = 14)


mplplt.show()