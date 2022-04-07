from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create 3 D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls and store the results in a list
results = [die_1.roll() + die_2.roll() + die_3.roll() for num_roll in range(50_000)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result+1)]

# Visualize data
x_values = list(range(3, max_result+1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Results'}

my_layout = Layout(title = 'Results from rolling 3 D6 50,000 times',
	xaxis = x_axis_config, yaxis = y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename = 'd6_d6_d6.html')