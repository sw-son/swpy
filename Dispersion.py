import math

num_friends = [3,5,7,10,13,17,20,24,28,40,50,55,58,62,65,69,75,80,92,100]
daily_minutes = [5,10,15,30,35,40,42,45,50,52,55,60,67,75,80,82,84,85,92,1]

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

