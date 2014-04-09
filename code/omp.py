#! /usr/bin/env python
"""
omp algorithm
different from sompy.py
omp.py uses batch omp to solve several omp problems at the same time.
These problems share the same dictionary, so some stuff can be calculated before
"""

import numpy as np
import scipy as scp

# solve the omp according to the constraint of sparsity
def ompsp(signal,dic,k):
	"""
	input:
		signal is the input singals
		dic is the dictionary
	output:

	"""
	try:
		dim = dic.shape[1]
	except IndexError:
		print "The shape of dictionary is wrong, please check again"
	except:
		print "Something unkown happened"

	n = min(dim,k) # in case k is out of range
	#initialization
	residual = signal
	notchosens = np.tile(np.arange(0,dim),(dic.shape[0],1))

def main():
	pass
if __name__ = '__main__':
	main()