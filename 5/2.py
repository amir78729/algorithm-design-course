import math
import csv
import operator as op
from functools import reduce
import time
from collections import defaultdict
import sys # Library for INT_MAX 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  for row in range(vertices)] 
  
    # A utility function to print the constructed MST stored in parent[] 
    def printMST(self, parent): 
        result = []
        print ("Edge \tWeight")
        for i in range(1, self.V): 
            result.append([parent[i], i, self.graph[i][ parent[i] ] ])
            # print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ] )
        return result
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minKey(self, key, mstSet): 
  
        # Initilaize min value 
        min = sys.maxsize 
  
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 
  
    # Function to construct and print MST for a graph  
    # represented using adjacency matrix representation 
    def primMST(self): 
  
        # Key values used to pick minimum weight edge in cut 
        key = [sys.maxsize] * self.V 
        parent = [None] * self.V # Array to store constructed MST 
        # Make key 0 so that this vertex is picked as first vertex 
        key[0] = 0 
        mstSet = [False] * self.V 
  
        parent[0] = -1 # First node is always the root of 
  
        for c in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minKey(key, mstSet) 
  
            # Put the minimum distance vertex in  
            # the shortest path tree 
            mstSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
  
                # graph[u][v] is non zero only for adjacent vertices of m 
                # mstSet[v] is false for vertices not yet included in MST 
                # Update the key only if graph[u][v] is smaller than key[v] 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
  
        result = self.printMST(parent) 
        return result


def distance(lat1,lon1,lat2,lon2):
    # dlat : latDistance ; dlon : lonDistance
	r = 6378.137 # radius of earth
	dlat = (lat2 - lat1) * math.pi / 180
	dlon = (lon2 - lon1) * math.pi / 180
	a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) * math.sin(dlon/2) * math.sin(dlon/2)
	return 2000 *r * math.atan2(math.sqrt(a),math.sqrt(1-a)) # distance in meters


class City:
    def __init__(self,name, x, y):
        self.name = name
        self.x = x
        self.y = y



		

def brute_force():
    global cities
    n = len(cities)
    distance_matrix = [[.0 for i in range(n)] for j in range(n)]
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            d = distance(cities[i].x, cities[i].y, cities[j].x, cities[j].y)
            # self.addEdge(i, j, d)
            distance_matrix[i][j] = d
            distance_matrix[j][i] = d
    return distance_matrix

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
g = Graph(len(cities))
print("> CALCULATING DESTINATIONS")
g.graph = brute_force()
print("> APPLYING PRIM ALGORITHM")
result = g.primMST()
print("> PRIM ALGORITHM'S RESULT")
cost = 0
print ("\t> Edges in the constructed MST")
for u, v, weight in result:
    cost += weight
    print("\t\t>  ~{} ( {} <-> {} )".format(round(weight), cities[u].name, cities[v].name))
print("\t> COST\n\t\t> " , cost)
print("> WRITING ON CSV FILE (india_cities_PRIM.csv)")
with open('india_cities_PRIM.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["city1_name", "city2_name", "weight"])
    for u, v, weight in result:
        writer.writerow([cities[u].name, cities[v].name, weight])
stop_time = time.time()
print("> TIME\n\t> ", stop_time - start_time, "s")
