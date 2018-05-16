import numpy as np

class Indicator(object):
	def SMA(self, array):
		'''return a single moving average of an price array, SMA = sum(array)/len(array)'''
		return sum(array)/len(array)

	def WMA(self, array):
		'''return a single weighted moving average of an price array, WMA = sum(WnPn), Wn = n/(1+2+...+n)'''
		n = len(array)
		WMA = (np.array(n) + 1) * array / sum(range(n))
		return WMA