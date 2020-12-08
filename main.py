from myUtil import *
from hanoi import *



def main(maxN = 8):
	print("")
	for N in range(1,maxN+1):
		domainInstance = generateHanoiInstance(N)
		print("hanoi(" + str(N) + ")")
		#print("Initial state: ", end="")
		#print(domainInstance)

		solution = hanoi(domainInstance)
		#print("Solution: ", end="")
		#print(solution, end="")
		#print("    ", end="")

		movesRequired = pow(2,N)-1
		movesMade = len(solution)
		if(movesRequired == movesMade):
			print("(moves: " + str(movesMade) + ")")
		else:
			print("main: Error,moves made (" + str(movesMade) + ") are not equal to the moves required (" + str(movesRequired) + ")")

		#print("Final state: ", end="")
		#print(domainInstance)

		if(N<maxN):
			print("--------------------------------------------------------------------------------")



main(20)