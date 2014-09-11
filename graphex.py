#Tim Jordan
#9/11/14

import pylab as pl
import numpy as np
#defining what the x variable will show up as
x=np.linspace(0,10,100)
#defining the function to be plotted
y=x**3-2*x-6
#plotting the function
pl.plot(x,y)
pl.show()