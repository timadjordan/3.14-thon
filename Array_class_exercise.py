"""
Coded by Tim Jordan
9/9/14
"""

from numpy import zeros, dot, sqrt
#creating the arrays
d1 = zeros([3],float)
d2 = zeros([3],float)
#inputing the values for vector 1
d1[0]=3
d1[1]=-4
d1[2]=2
#inputing the values for vector 2
d2[0]=2
d2[1]=1
d2[2]=-1.5
#taking the magnitude of the vectors
mag1 = sqrt(sum(d1))
mag2 = sqrt(sum(d2))
#printing the magnitudes and the dot product of the vectors
print 'The magnitude of vector 1 is:', mag1 
print 'The magnitude of vector 2 is:', mag2
print 'The dot product of the two vectors is:', dot(d1,d2)