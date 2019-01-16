import math

num_friends = [70,65,72,63,71,64,60,67,100,1,5,7,9,43,21,35,20,3,8,20]
daily_minutes = [20,10,15,40,60,5,30,42,1,75,100,23,24,31,4,9,10,55,5,80]

''' Max data - Min data '''

def data_range(x):
	return max(x) - min(x)

''' deviations, variance '''

def dot(v,w):
	return sum(v_i * w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v):
	return dot(v,v)

def mean(x):
	return sum(x) / len(x)

def de_mean(x):
	x_bar = mean(x)
	return [x_i - x_bar for x_i in x]
	
def variance(x):
	n = len(x)
	deviations = de_mean(x)
	return sum_of_squares(deviations) / (n - 1)
	'''
	cuz n - 1 : bias To correction for small calculations
	'''

''' standard_deviation '''

def standard_deviation(x):
	return math.sqrt(variance(x))

''' interquartile range '''

def interquartile_range(x):
	return quantile(x,0.75) - quantile(x,0.25)

''' covariance ''' 

def covariance(x, y):
	n = len(x)
	return dot(de_mean(x),de_mean(y)) / (n - 1)

''' correlation '''

def correlation(x ,y):
	stdev_x = standard_deviation(x)
	stdev_y = standard_deviation(y)
	if stdev_x > 0 and stdev_y > 0:
		return covariance(x, y) / stdev_x / stdev_y
	else:
		return 0
	
''' outlier '''

outlier = num_friends_index(100)

num_friends_good = [x for x, i in enumerate(num_friends) if i != outlier]
daily_minutes_good = [x for x, i in enumerate(daily_minutes) if i != outlier]

correlation(num_friends_good, daily_minutes_good)

