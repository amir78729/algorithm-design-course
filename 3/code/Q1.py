# Python program for implementation of Radix Sort 
# A function to do counting sort of arr[] according to 
# the digit represented by exp. 
MAX = 256

def split(word): 
    return [char for char in word]
# def countingSort(arr, exp1): 

# 	n = len(arr) 

# 	# The output array elements that will have sorted arr 
# 	output = [0] * (n) 

# 	# initialize count array as 0 
# 	count = [0] * (27) 

# 	# Store count of occurrences in count[] 
# 	for i in range(0, n): 
# 		index = (arr[i] / exp1) 
# 		count[int(index % 10)] += 1

# 	# Change count[i] so that count[i] now contains actual 
# 	# position of this digit in output array 
# 	for i in range(1, 10): 
# 		count[i] += count[i - 1] 

# 	# Build the output array 
# 	i = n - 1
# 	while i >= 0: 
# 		index = (arr[i] / exp1) 
# 		output[count[int(index % 10)] - 1] = arr[i] 
# 		count[int(index % 10)] -= 1
# 		i -= 1

# 	# Copying the output array to arr[], 
# 	# so that arr now contains sorted numbers 
# 	i = 0
# 	for i in range(0, len(arr)): 
# 		arr[i] = output[i] 

# Method to do Radix Sort 
def radixSort(arr, n, max_len): 

	# Find the maximum number to know number of digits 
	# max1 = max(arr) 
	output = []
	count = []
	for i in range(max_len):
		count = [0] * (MAX + 1)

		for j in range(n):
			output.append(arr[j])

		# print(output)
		for j in range(n):
			try:
				count[arr[j][i]] = count[arr[j][i]] + 1
			except:
				count[0] = count[0] + 1
		# print(count)
		for j in range(1,MAX+1):################
			count[j] += count[j - 1]
		
		# print(count)
		for j in range(n-1 ,0):
			print(arr[j])
			try:
				output[count[arr[j][i]] - 1] = arr[j]
				count[arr[j][i]] = count[arr[j][i]] - 1
			except :
				output[count[0] - 1] = arr[j]
				count[0] = count[0] - 1
		for j in range(n):
			arr[j] = output[j]
			print(output[j], end=" ")
		if i != max_len - 1:
			print("")
		output = []
			



	# Do counting sort for every digit. Note that instead 
	# of passing digit number, exp is passed. exp is 10^i 
	# where i is current digit number 
    
	# exp = 1
	# while max1 / exp > 0: 
	# 	# countingSort(arr, exp) 
	# 	exp *= 10


# Driver code 
# arr = [170, 45, 75, 90, 802, 24, 2, 66] 
# arr = ["aab","adfv","dkkkkkkkkkkkkkkkkkkkkkkkkkd","dfdf"] 
arr = []
n = input()
n = int(n)
maxlen = 0
for i in range(n):
	s = input()
	# arr.append(split(s))
	arr.append(s)
	if maxlen < len(s):
    		maxlen = len(s)
# Function Call 
# radixSort(arr) 
# print(arr)
# print(max_len)
radixSort(arr, n, maxlen) 

# for i in range(len(arr)):
#     if len(arr[i]) < max_len:

# for i in range(len(max(arr))):
#     for j in range(len(arr)):
#         print(arr[i][j])
# for i in range(len(arr)): 
# 	print(arr[i]) 

# This code is contributed by Mohit Kumra 
# Edited by Patrick Gallagher 
