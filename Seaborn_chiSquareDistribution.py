from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
"""
Chi Square Distribution
Chi Square distribution is used as a basis to verify the hypothesis.
It has two parameters:"""
#df - (degree of freedom).
#size - The shape of the returned array.
#Draw out a sample for rayleigh distribution with scale of 2 with size 2x3:
x = random.chisquare(df=2, size=(2, 3))
print(x) 

"""Visualization of Chi Square Distribution"""
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show() 

"""Similarity Between Rayleigh and Chi Square Distribution"""
#At unit stddev the and 2 degrees of freedom rayleigh and chi square represent the same distributions. 
