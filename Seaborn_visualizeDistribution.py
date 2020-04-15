#Import Matplotlib
#import the pyplot object of the Matplotlib module in your code using following code 
import matplotlib.pyplot as plt 

#Import Seaborn
#import the seaborn in your code using following code 
import seaborn as sns 

"""Distplots
Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array. """

"""Visualize Distributions With Seaborn
Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions."""

"""Plotting a Displot """
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show() 

"""Plotting a Distplot Without the Histogram"""
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show() 
#We will be using: sns.distplot(arr, hist=False) to visualize random distributions in this tutorial.