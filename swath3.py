# importing the required module
import matplotlib.pyplot as plt
 
# x axis values
x = [5,10,15,20,25]
# corresponding y axis values
y = [177,198,200,202,204]
 
# plotting the points 
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('My first graph!')
 
# function to show the plot
plt.show()