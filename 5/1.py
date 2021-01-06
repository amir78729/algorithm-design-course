import math
import csv
import operator as op
from functools import reduce
import time
from collections import defaultdict

def distance(lat1,lon1,lat2,lon2):
    # dlat : latDistance ; dlon : lonDistance
	r = 6378.137 # radius of earth
	dlat = (lat2 - lat1) * math.pi / 180
	dlon = (lon2 - lon1) * math.pi / 180
	a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) * math.sin(dlon/2) * math.sin(dlon/2)
	return 2000 *r * math.atan2(math.sqrt(a),math.sqrt(1-a)) # distance in meters

# def nCr(n,r): ############ OVERFLOW!!!!!!!
#     f = math.factorial
#     return f(n) / f(r) / f(n-r)

def nCr(n, r):
    r = min(r, n-r)
    n = reduce(op.mul, range(n, n-r, -1), 1)
    d = reduce(op.mul, range(1, r+1), 1)
    return n // d


class City:
    def __init__(self,name, x, y):
        self.name = name
        self.x = x
        self.y = y


class Graph:
	def __init__(self, vertices):
		self.V = vertices 
		self.graph = [] 


	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])


	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])


	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		else:
			parent[yroot] = xroot
			rank[xroot] += 1


	def KruskalMST(self):   
		result = [] # This will store the resultant MST	
		i = 0 # An index variable, used for sorted edges	
		e = 0 # An index variable, used for result[]
		# Step 1: Sort all the edges in  non-decreasing order of their weight. If we are not allowed to change the given graph, we can create a copy of graph
		self.graph = sorted(self.graph, key=lambda item: item[2])
		parent = []
		rank = []
		# Create V subsets with single elements
		for node in range(self.V):
			parent.append(node)
			rank.append(0)
		# Number of edges to be taken is equal to V-1
		while e < self.V - 1:
			try:
			    # Step 2: Pick the smallest edge and increment the index for next iteration
				u, v, w = self.graph[i]
				i = i + 1
				x = self.find(parent, u)
				y = self.find(parent, v)
			    # If including this edge does't cause cycle, include it in result and increment the indexof result for next edge
				if x != y:
					e = e + 1
					result.append([u, v, w])
					self.union(parent, rank, x, y)
			except:
				break
		return result
		

	def brute_force(self):
		global cities
		n = len(cities)
		for i in range(0, n - 1):
			for j in range(i + 1, n):
				d = distance(cities[i].x, cities[i].y, cities[j].x, cities[j].y)
				self.addEdge(i, j, d)

file_name ='india_cities.csv'
cities = []
start_time = time.time()
print("> READING FROM CSV FILE")
with open(file_name,  encoding="utf-8" , errors='ignore') as file:
	reader = csv.reader(file)
	for row in reader:
		try:		
			cities.append(City(str(row[1]),float(row[2]), float(row[3])))
			n = n + 1
		except :
			pass
print("\t> CITIES")
for c in cities:
    print("\t\t> {}: ( {}, {} )".format(c.name, c.x, c.y))	
print("\t> NUMBER OF CITIES\n\t\t> ",len(cities))
g = Graph(nCr(len(cities),2))
print("> CALCULATING DESTINATIONS")
g.brute_force()
print("> APPLYING KRUSKAL ALGORITHM")
result = g.KruskalMST()
print("> KRUSKAL ALGORITHM'S RESULT")
cost = 0
print ("\t> Edges in the constructed MST")
for u, v, weight in result:
    cost += weight
    print("\t\t>  ~{} ( {} <-> {} )".format(round(weight), cities[u].name, cities[v].name))
print("\t> COST\n\t\t> " , cost)
print("> WRITING ON CSV FILE (india_cities_KRUSRAL.csv)")
with open('india_cities_KRUSRAL.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["city1_name", "city2_name", "weight"])
    for u, v, weight in result:
        writer.writerow([cities[u].name, cities[v].name, weight])
stop_time = time.time()
print("> TIME\n\t> ", stop_time - start_time, "s")
