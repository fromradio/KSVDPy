# single omp algorithm
# omp algorithm for a single vector
#! /usr/bin/env python

import numpy as numpy

def somp(vec,dic,sp = 5):
	"""
	omp algorithm for a single vector
	input:
		vec -- the input vector
		dic -- the dictionary
	basic assumptions:
		the dictionary is supposed to be normalized before running the function
	"""
	# vec = dic*alpha
	# alpha is a sparse coordinate
	dim = dic.shape[1]
	# in case that dim is smaller than sp
	n = min(dim,sp)

	for i in range(0,n):
		# find the corresponding vectors
		pass
	
def main():
	dic = np.array([[1,0],[0,1]])
	vec = np.array([1,0])

if __name__ == '__main__':
	main()