import math 
import copy
import csv 

class Point(): 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 
def distance_between_2_points(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))

def brute_force(A, n):
    min = math.inf
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            d = distance_between_2_points(A[i], A[j])
            if d < min :
                min = d
    return min
# def stripClosest(strip, size, d): 
# 	min_val = d 
# 	for i in range(size): 
# 		j = i + 1
# 		while j < size and (strip[j].y -strip[i].y) < min_val: 
# 			min_val = distance_between_2_points(strip[i], strip[j]) 
# 			j += 1
# 	return min_val 

# def closestUtil(P, Q, n): 
# 	if n <= 3: 
# 		return brute_force(P, n) 
# 	mid = n // 2
# 	midPoint = P[mid] 
# 	dl = closestUtil(P[:mid], Q, mid) 
# 	dr = closestUtil(P[mid:], Q, n - mid) 
# 	d = min(dl, dr) 
# 	strip = [] 
# 	for i in range(n): 
# 		if abs(Q[i].x - midPoint.x) < d: 
# 			strip.append(Q[i]) 
	
# 	# i = mid
# 	# while abs(Q[i].x - midPoint.x) < d: 
# 	# 		strip.append(Q[i]) 
# 	# 		i -= 1
# 	# i = mid
# 	# while abs(Q[i].x - midPoint.x) < d: 
# 	# 		strip.append(Q[i]) 
# 	# 		i += 1


# 	return min(d, stripClosest(strip, len(strip), d)) 
 
# def closest(P, n): 
# 	P.sort(key = lambda point: point.x) 
# 	Q = copy.deepcopy(P)
# 	# Q = P
# 	Q.sort(key = lambda point: point.y)	 

# 	return closestUtil(P, Q, n) 


# P = []
# n = input()
# for i in range(int(n)):
#     x, y = input().split() 
#     P.append(Point(float(x), float(y)))
# result = closest(P, int(n))
# print(round(result, 5))

P = []
n = 0
file_name ='test6.csv'
# file_name ='test5.csv'
# file_name ='test4.csv'
# file_name ='test3.csv'
# file_name ='test2.csv'
# file_name ='test1.csv'
with open(file_name,  encoding="utf-8" , errors='ignore') as file:
	reader = csv.reader(file)
	for row in reader:
		try:		
			P.append(Point(float(row[1]), float(row[2])))
			n = n + 1
		except:
			pass
				
print(file_name)
print("# of points: ",len(P))


for c in P:
    print("{}/{}".format(c.x, c.y))

# print(n)
# result = closest(P, int(n))
# print("result for recursive method: ",round(result, 5))
result = brute_force(P, int(n))
print("result for recursive method: ",round(result, 5))

