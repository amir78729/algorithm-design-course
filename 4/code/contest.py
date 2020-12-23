"""The following implementation assumes that the activities 
are already sorted according to their finish time"""

"""Prints a maximum set of activities that can be done by a 
single person, one at a time"""
# n --> Total number of activities 
# s[]--> An array that contains start time of all activities 
# f[] --> An array that contains finish time of all activities 

def printMaxActivities( ): 
	print ("The following activities are selected")

	# The first activity is always selected 
	i = 0
	print (i)

	# Consider rest of the activities 
	for j in range(k): 

		# If this activity has start time greater than 
		# or equal to the finish time of previously 
		# selected activity, then select it 
		if s[j] >= f[i]: 
			print (j,"}") 
			i = j 

# Driver program to test above function 
s = [] 
f = [] 


# printMaxActivities(s, f) 

n, k = input().split()
n, k = int(n),int(k)
for index in range(k):
    l, r = input().split()
    s.append(int(l))
    f.append(int(r))
# print(k)
# print(s)
# print(f)
if n <= k:
    printMaxActivities(s, f) 
else:
    print("FALSE")


# This code is contributed by Nikhil Kumar Singh 
