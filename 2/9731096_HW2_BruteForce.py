import math

class Point:
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
        
P = []
n = input()
for i in range(int(n)):
    x, y = input().split() 
    P.append(Point(int(x), int(y)))
print(round(brute_force(P, int(n)), 5))

