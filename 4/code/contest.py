"""The following implementation assumes that the activities 
are already sorted according to their finish time"""

"""Prints a maximum set of activities that can be done by a 
single person, one at a time"""
# n --> Total number of activities 
# s[]--> An array that contains start time of all activities 
# f[] --> An array that contains finish time of all activities 

def printMaxActivities( ): 
	global res
	# print ("The following activities are selected") 
    # res = 0
	# The first activity is always selected 
	i = 0
    
	# print (i)

	# Consider rest of the activities 
	for j in range(k): 

		# If this activity has start time greater than 
		# or equal to the finish time of previously 
		# selected activity, then select it 
        # if s[j] >= f[i]: 
		if s[j][0] >= s[i][1]: 
            # res = 1 + res
			res += 1
			i = j 
            


# take second element for sort
def takeSecond(elem):
    return elem[1]

# Driver program to test above function 
s = [] 
f = [] 

res = 0
# printMaxActivities(s, f) 

n, k = input().split()
n, k = int(n),int(k)
for index in range(k):
    l, r = input().split()
    # s.append(int(l))
    # f.append(int(r))
    tmp = []
    s.append(tmp)
    s[index].append(int(l))
    s[index].append(int(r))

s.sort(key=takeSecond)
# print(k)
# print(s)
# print(f)
if n <= k:
    printMaxActivities() 
    print("YES")
else:
    print("NO")


# This code is contributed by Nikhil Kumar Singh 
