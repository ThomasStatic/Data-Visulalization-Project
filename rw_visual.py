import matplotlib.pyplot as mplplt

from random_walk import RandomWalk

# Make a random walk
rw = RandomWalk(5000)
rw.fill_walk()

# Plot the points in the walk
mplplt.style.use('classic')
fig,ax = mplplt.subplots(figsize = (15,9))
point_numbers = range(rw.num_points)
# ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = mplplt.cm.Blues, edgecolors = 'none', s = 1)
ax.plot(rw.x_values, rw.y_values, linewidth = 1)

# Emphasize the first and last points
ax.scatter(0,0, c ='green', edgecolors = 'none', s = 100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)

# Remove the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


mplplt.show()