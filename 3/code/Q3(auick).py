import random

comp = 0

def compare(A, B): 
	global comp
	if len(A) == len(B):
		n = len(A)
		for i in range(n):
			if A[n-i-1] == B[n-i-1]:
				comp+=1 
				pass
			else:
				comp+=1 
				return (A[n-i-1] > B[n-i-1])
	else:
		comp+=1 
		if (len(A) > len(B)):
			return True
		else:
			return False

def partition_rand(arr , start, stop):
    	
    random_pivot = random.randrange(start, stop)

    arr[start], arr[random_pivot] = arr[random_pivot], arr[start]
    return partition(arr, start, stop)
	
def partition(arr,low,high): 
	global comp
	i = ( low-1 )		
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		if not compare(arr[j], pivot): 
		
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

def quickSort(arr,low,high): 
	global comp
	if low < high:
		comp+=1 

		pi = partition_rand(arr,low,high) 

		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 

if __name__ == "__main__":
	arr = []
	# n = input() 
	# n = int(n)
	# for i in range(int(n)):
	# 	s = input()
	# 	arr.append((s))
	filename = 'input11.txt'
	file1 = open(filename, 'r') 
	Lines = file1.readlines() 
	first = True
	# print(Lines)
	for line in Lines: 
		if first:
			# print(line)
			n = line
			n = int(n)
			first = False
		else:
			if line.endswith('\n'):
				line = line[:-1] 
			arr.append(line)


	quickSort(arr,0,n-1) 
	for i in range(n): 
		print (arr[i]) 
		# pass

	# print(comp)
