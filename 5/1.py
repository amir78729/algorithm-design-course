import math
import csv
import operator as op
from functools import reduce

def distance(lat1,lon1,lat2,lon2):
    # dlat : latDistance ; dlon : lonDistance
	r = 6378.137 # radius of earth
	dlat = (lat2 - lat1) * math.pi / 180
	dlon = (lon2 - lon1) * math.pi / 180
	a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) * math.sin(dlon/2) * math.sin(dlon/2)
	return 2000 *r * math.atan2(math.sqrt(a),math.sqrt(1-a)) # distance in meters

# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph

from collections import defaultdict

# def nCr(n,r):
#     f = math.factorial
#     return f(n) / f(r) / f(n-r)

def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom
# Class to represent a graph

class City:
    def __init__(self,name, x, y):
        self.name = name
        self.x = x
        self.y = y


class Graph:

	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.graph = [] # default dictionary
		# to store graph

	# function to add an edge to graph
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	# A utility function to find set of an element i
	# (uses path compression technique)
	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	# A function that does union of two sets of x and y
	# (uses union by rank)
	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		# Attach smaller rank tree under root of
		# high rank tree (Union by Rank)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot

		# If ranks are same, then make one as root
		# and increment its rank by one
		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	# The main function to construct MST using Kruskal's
		# algorithm
	def KruskalMST(self):

		result = [] # This will store the resultant MST
		
		# An index variable, used for sorted edges
		i = 0
		
		# An index variable, used for result[]
		e = 0

		# Step 1: Sort all the edges in 
		# non-decreasing order of their
		# weight. If we are not allowed to change the
		# given graph, we can create a copy of graph
		self.graph = sorted(self.graph, 
							key=lambda item: item[2])

		parent = []
		rank = []

		# Create V subsets with single elements
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# Number of edges to be taken is equal to V-1
		while e < self.V - 1:
			try:
			# Step 2: Pick the smallest edge and increment
			# the index for next iteration
			# print(i)
				u, v, w = self.graph[i]
				i = i + 1
				x = self.find(parent, u)
				y = self.find(parent, v)

			# If including this edge does't
			# cause cycle, include it in result 
			# and increment the indexof result 
			# for next edge
				if x != y:
					e = e + 1
					result.append([u, v, w])
					self.union(parent, rank, x, y)
			# Else discard the edge
			except:
				break

		minimumCost = 0
		print ("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			# print("%d -- %d == %d" % (u, v, weight))
			print("- ~{} ( {} <-> {} )".format(round(weight), cities[u].name, cities[v].name))
		print("Minimum Spanning Tree" , minimumCost)

def brute_force():
    # min = math.inf
    global cities
    global g
    n = len(cities)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            d = distance(cities[i].x, cities[i].y, cities[j].x, cities[j].y)
            # g.addEdge(cities[i], cities[j], d)
            g.addEdge(i, j, d)
    # return min

# Driver code




file_name ='india_cities.csv'
# file_name ='test5.csv'
# file_name ='test4.csv'
# file_name ='test3.csv'
# file_name ='test2.csv'
# file_name ='test1.csv'

cities = []
with open(file_name,  encoding="utf-8" , errors='ignore') as file:
	reader = csv.reader(file)
	for row in reader:
		try:		
			cities.append(City(str(row[1]),float(row[2]), float(row[3])))
			n = n + 1
		except :
			pass
				
print(file_name)
print("# of cities: ",len(cities))

# for c in cities:
#     print("{}: {}::{}".format(c.name, c.x, c.y))


# brute_force()
print(nCr(10, 2))

g = Graph(nCr(len(cities),2))
# g.addEdge(0, 1, 10)
# g.addEdge(0, 2, 6)
# g.addEdge(0, 3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)
brute_force()

# Function call
g.KruskalMST()

# This code is contributed by Neelam Yadav
