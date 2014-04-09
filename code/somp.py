# single omp algorithm
# omp algorithm for a single vector
#! /usr/bin/env python

import numpy as np
import scipy.linalg as linalg

def somp(vec,dic,sp = 5):
	"""
	omp algorithm for a single vector
	input:
		vec -- the input vector
		dic -- the dictionary
	return:
		a tuple (chosen,alpha,residual)
		'chosen' is the chosen indices of the corresponding atom functions
		'alpha' is the corresponding coordinate
		'residual' is the residual of the fitting
	basic assumptions
		the dictionary is supposed to be normalized before running the function
	"""
	# vec = dic*alpha
	# alpha is a sparse coordinate
	dim = dic.shape[1]
	# in case that dim is smaller than sp
	n = min(dim,sp)
	# initialization
	residual = vec 		# residual
	notchosen = range(0,dim)
	chosen = []
	for i in range(0,n):
		# find the corresponding vectors
		# first sweeping:
		e = np.dot(dic.T[notchosen,:],vec)
		e = np.abs(e)
		# support update
		ind = notchosen[e.argmax()]
		notchosen.remove(ind)
		chosen.append(ind)
		# provision
		A = dic[:,chosen]
		r = linalg.lstsq(A,vec)
		alpha = r[0]
		residual = r[1]
	return (chosen,alpha,residual)
	
"""
main function is used for test
"""
def main():
	#dic = np.array([[1,0,0],[0,1,0],[0,0,1]])
	dic = np.random.rand(100,200)
	dic /= np.linalg.norm(dic,axis = 0 )
	#print "norm of dic is ",np.linalg.norm(dic,axis=0)
	#vec = np.array([1,0,1])
	vec = np.random.rand(100)
	a = somp(vec,dic,99)
	print a

if __name__ == '__main__':
	main()