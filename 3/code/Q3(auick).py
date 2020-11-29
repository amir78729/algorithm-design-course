import random

def compare(A, B): 
	if len(A) == len(B):
		n = len(A)
		for i in range(n):
			if A[n-i-1] == B[n-i-1]:
				pass
			else:
				return (A[n-i-1] > B[n-i-1])
	else:
		if (len(A) > len(B)):
			return True
		else:
			return False

def partition_rand(arr , start, stop):
    	
    random_pivot = random.randrange(start, stop)

    arr[start], arr[random_pivot] = arr[random_pivot], arr[start]
    return partition(arr, start, stop)
	
def partition(arr,low,high): 
	i = ( low-1 )		
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		if not compare(arr[j], pivot): 
		
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

def quickSort(arr,low,high): 
	if low < high: 

		pi = partition_rand(arr,low,high) 

		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 

if __name__ == "__main__":
	arr = []
	n = input() 
	n = int(n)
	for i in range(int(n)):
		s = input()
		arr.append((s))
	quickSort(arr,0,n-1) 
	for i in range(n): 
		print (arr[i]) 

