FIRST = 0
SECOND = 1
THIRD = 2



def generateHanoiInstance(N):
	domainInstance = [[],[],[]]
	#fix possibly invalid input
	if(N<1):
		N=1
	# generate first column
	for i in range(0,N):
		domainInstance[FIRST].append(N-i)
	# return generated instance
	return domainInstance



def isValid(domainInstance):
	# 2nd & 3rd column should be empty,initially 
	if(  (len(domainInstance[SECOND]) > 0)  or  (len(domainInstance[THIRD]) > 0)  ):
		return False

	# 1st column shall not be empty...
	N = len(domainInstance[FIRST])
	if(N==0):
		return False
	# ...as it shall contain all numbers from 1 to N,in descending order (N,N-1,...,2,1)
	pos = 0
	for i in range(0,N):
		if( domainInstance[FIRST][i] != (N-i) ):
			return False

	return True