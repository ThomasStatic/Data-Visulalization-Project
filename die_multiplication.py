from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create 2 D6 dies
die_1 = Die()
die_2 = Die()

# Make some rolls and store results in a list
results = []
for roll_num in range(50_000):
	result = die_1.roll() * die_2.roll()
	results.append(result)

# Analyze results
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualize results

x_values = list(range(1, max_result+1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequencies of Results'}

my_layout = Layout(title = 'Product of results of rolling 2 D6 50,000 times',
	xaxis = x_axis_config, yaxis = y_axis_config)

offline.plot({'data':data, 'layout':my_layout}, filename = 'd6_d6_product.html')