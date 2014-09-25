# Simpson's approximation error

#I started by defining the function that
# was to be integrated
def f(x):
	return (x**4)-2*(x**2)-1
	
# Then I defined another function that used
# Simpson's method for approximate integration 
def sim(N):	
	N=int(N)
	a=0.0
	b=2.0
	step=(b-a)/N

	S = f(a)+f(b)

	for counter in range(1,N):
		new_x = a+counter*step
		if counter%2==0:
			S += 2.0*f(new_x)
		else:
			S += 4.0*f(new_x)

	S=step*S/3.0
	return S

Q=sim(1000)
R=sim(500)
S=1.0/15.0*(Q-R)

print "Simpson's rule resulting integral:",Q
print "Simpson's rule resulting error: %2.16f" % S


# Trapezoidal approximation error
# I followed the same method as before, 
# but this time I used the trapezoidal method.
def g(x):
	return (x**4)-2*(x**2)-1
	
def trap(M):
	M=int(M)
	c=0.0
	d=2.0
	jump=(d-c)/M
	
	T = .5*f(c)+.5*f(d)
	
	for counter in range (1,M):
		new_z = c+counter*jump
		T += g(new_z)			
	T=jump*T
	return T
	
U=trap(1000)
V=trap(500)
W=1.0/3.0*(U*V)

print "Trapezoid method resulting integral:",U
print "Trapzoid method resulting error: %2.16f" % W