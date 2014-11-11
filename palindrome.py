# Coded By Tim Jordan
# Palindrome finder

# Inputing phrase and turning it into a list
S = raw_input('Please input your sentence: ')
S=list(S)

# Defining the Palindrome function
def palindrome(S):
	l = len(S)
# Using recursion to loop through the list	
	if S == []:
		print "It's a Palindrome"
	elif S[0] == S[l-1]:
		return palindrome(S[1:l-1])
	else:
		print "Not a Palindrome!"
palindrome(S)