import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,11)
y=np.random.randint(10,100,size=10)

#line plot
plt.figure(figsize=(6,4))
plt.plot(x,y,marker='*',color='b',linestyle='-',label='line plot')
plt.title('line plot example')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc='lower right')
plt.show()

#barchart
plt.figure(figsize=(6,4))
plt.bar(x,y,color='indigo')
plt.title('bar chart example')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

# Scatter plot
plt.figure(figsize=(6,6))
plt.scatter(x,y,color='blue',marker='*')
plt.title('Scatter plot example')
plt.xlabel('Scatter x-axis')
plt.ylabel('Scatter y-axis')
plt.show()