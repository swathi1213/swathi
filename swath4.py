import matplotlib.pyplot as plt
 
# x-coordinates of left sides of bars 
left = [1, 2, 3, 4]
 
# heights of bars
height = [10, 24, 36, 40]
 
# labels for bars
tick_label = ['one', 'two', 'three', 'four']
 
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['r', 'g','b'])
 
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')
 
# function to show the plot
plt.show()