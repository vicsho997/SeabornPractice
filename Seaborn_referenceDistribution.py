from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

"""Multinomial distribution is a generalization of binomial distribution.
It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.
It has three parameters:"""

"""Difference Between Poisson and Binomial Distribution"""
#Normal distribution is continous whereas poisson is discrete.
#But we can see that similar to binomial for a large enough poisson distribution it will become similar to normal distribution with certain std dev and mean.

"""Difference Between Poisson and Binomial Distribution"""
#The difference is very subtle it is that, binomial distribution is for discrete trials, whereas poisson distribution is for continuous trials.
#But for very large 'n' and near-zero 'p' binomial distribution is near identical to poisson distribution such that 'n * p' is nearly equal to 'lam'.

"""Difference Between Logistic and Normal Distribution"""
#Both distributions are near identical, but logistic distribution has more area under the tails. ie. It representage more possibility of occurence of an events further away from mean.
#For higher value of scale (standard deviation) the normal and logistic distributions are near identical apart from the peak.

"""Relation Between Poisson and Exponential Distribution"""
#Poisson distribution deals with number of occurences of an event in a time period whereas exponential distribution deals with the time between these events. 

"""Similarity Between Rayleigh and Chi Square Distribution"""
#At unit stddev the and 2 degrees of freedom rayleigh and chi square represent the same distributions. 


"""Poisson Distribution"""
#lam - rate or known number of occurences e.g. 2 for above problem.
#size - The shape of the returned array.

"""Uniform Distribution """
#a - lower bound - default 0 .0.
#b - upper bound - default 1.0.
#size - The shape of the returned array.

"""Logistics Distribution"""
#loc - mean, where the peak is. Default 0.
#scale - standard deviation, the flatness of distribution. Default 1.
#size - The shape of the returned array.

"""Multinomial Distribution"""
#n - number of possible outcomes (e.g. 6 for dice roll).
#pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
#size - The shape of the returned array.

"""Exponential Distribution"""
#scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
#size - The shape of the returned array.

"""Rayleigh Distribution"""
#scale - (standard deviation) decides how flat the distribution will be default 1.0).
#size - The shape of the returned array.

"""Chi Square Distribution"""
#df - (degree of freedom).
#size - The shape of the returned array.

"""Pareto Distribution"""
#a - shape parameter.
#size - The shape of the returned array.