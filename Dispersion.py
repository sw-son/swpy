import math

score = [10,30,50,70,90]
''' Max data - Min data '''

def data_range(x):
	return max(x) - min(x)

''' deviations, variance '''

def mean(x):
	return sum(x) / len(x)

def de_mean(x):
	x_bar = mean(x)
	return [x_i - x_bar for x_i in x]
	
def variance(x):
	n = len(x)
	deviations = de_mean(x)
	sum_of_squares = sum([x_i ** 2 for x_i in deviations])
	return sum_of_squares / (n - 1)
	'''
	cuz n - 1 : bias To correction for small calculations
	'''

''' standard_deviation '''

def standard_deviation(x):
	return math.sqrt(variance(x))

''' interquartile range '''

def interquartile_range(x):
	return quantile(x,0.75) - quantile(x,0.25)


