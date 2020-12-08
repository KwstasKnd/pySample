from myUtil import *



def hanoi(domainInstance):
	if( isValid(domainInstance) ):
		N = len(domainInstance[0])
		return rec_hanoi(domainInstance,N,FIRST,THIRD) # move N disks from column 1 to column 3
	else:
		print("hanoi: Error,invalid domainInstance given as argument")
		return ["ERROR"]



def rec_hanoi(columns,N,From,To):
	if(N==1):
		top = (len(columns[From]) - 1)
		disk = columns[From][top]
		columns[From].remove(disk)
		columns[To].append(disk)
		move = str(From+1) + "-->" + str(To+1)
		return [move]
	
	Other = -1
	for c in range(0,2+1):
			if( (From != c) and (To != c) ):
				Other = c
				break
	# Goal: move N disks from columns[From] to column columns[To],using columns[Other] as an intermediate
	
	# Step 1: move the N-1 smaller disks from columns[From] to column columns[Other]
	moves1 = rec_hanoi(columns,N-1,From,Other)

	# Step 2: move the larger disk from columns[From] to column columns[To]
	moves2 = rec_hanoi(columns,1,From,To)

	# Step 3: move the N-1 smaller disks from columns[Other] to column columns[To]
	moves3 = rec_hanoi(columns,N-1,Other,To)
	
	return moves1 + moves2 + moves3

# added by hub
