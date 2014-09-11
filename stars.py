#Tim Jordan
#9/11/14

#This program pulls data from the text file stars.txt and plots them
import numpy as np
import pylab as pl
#Importing the data
s = np.loadtxt("/Users/boredom264/GitHub/Exercises/Data/stars.txt", float)
#plotting the data
pl.scatter(s[:,0],s[:,1])
pl.show() 