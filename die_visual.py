from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two d6
die_1 = Die()
die_2 = Die()


# Make some results and store the results in a list
roll_num = range(1000)
results = [die_1.roll() + die_2.roll() for x in roll_num]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
value_range = range(2, max_result + 1)
frequencies = [results.count(value) for value in value_range]
# for value in range(2, max_result + 1):
# 	frequency = results.count(value)
# 	frequencies.append(frequency)

# Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y = frequencies)]

# Setting dtick to 1 tells plotly to label every tick
x_axis_config = {'title': 'Result', 'dtick':1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(title = "Results of rolling two D6 1000 times",
 xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename = 'd6_d6.html')
