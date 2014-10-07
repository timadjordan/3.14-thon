# Tim Jordan
# 10/7/14
# Derivative Exercise

import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x**3-np.sin(x)

# defining constants	
x0 = 2	
h = .00000001
h1 = .00001
fd = (f(x0+h)-f(x0))/h #forwarddifference
cd = (f(x0+h1/2)-f(x0-h1/2))/h1 #centraldifference 
av = 3*2**2-np.cos(2) #actualdifference

# finding errors
errorfd = abs(fd-av)/av
errorcd = abs(cd-av)/av

print "The forward difference is:", fd
print "The error for forward difference is:", errorfd
print "The central difference is:", cd
print "The error for central difference is:", errorcd
print "#accuracy"