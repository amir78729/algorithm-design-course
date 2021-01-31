import math

def generate_nodes(level, xxx):
    if not (level in nodes):
        node = {}
        count = 1
        for i in range(n):
            for j in range(m):
                if park[i][j] != 'f' or count in xxx:
                    current_list = []
                    if i > 0:
                        if park[i-1][j] != 'f':
                            current_list.append((i-1)* m + j + 1)
                    if j > 0:
                        if park[i][j-1] != 'f':
                            current_list.append(i*m + (j-1) + 1)
                    if i < n-1:
                        if park[i+1][j] != 'f':
                            current_list.append((i+1)* m + j + 1)
                    if j < m-1:
                        if park[i][j+1] != 'f':
                            current_list.append(i * m + (j+1) + 1)
                    node.update({count: current_list})
                count += 1
        nodes.update({level: node})

def spreadFire(level, lastLevel):
    if level > lastLevel[0]:
        lastLevel[0] += 1
        fires_c = fires.copy()
        for fire in fires_c:
            if fire[0] > 0:
                park[fire[0] - 1][fire[1]] = 'f'
                fires.add((fire[0]-1, fire[1]))
                if fire[1] > 0:
                    fires.add((fire[0]-1, fire[1] - 1))
                    park[fire[0] - 1][fire[1] - 1] = 'f'
                if fire[1] < m-1:
                    fires.add((fire[0]-1, fire[1] + 1))
                    park[fire[0] - 1][fire[1] + 1] = 'f'

            if fire[0] < n-1:
                fires.add((fire[0]+1, fire[1]))
                park[fire[0] + 1][fire[1]] = 'f'
                if fire[1] > 0:
                    fires.add((fire[0] + 1, fire[1] - 1))
                    park[fire[0] + 1][fire[1] - 1] = 'f'
                if fire[1] < m-1:
                    fires.add((fire[0]+1, fire[1] + 1))
                    park[fire[0] + 1][fire[1] + 1] = 'f'

            if fire[1] > 0:
                fires.add((fire[0], fire[1] - 1))
                park[fire[0]][fire[1] - 1] = 'f'
            if fire[1] < m-1:
                fires.add((fire[0], fire[1] + 1))
                park[fire[0]][fire[1] + 1] = 'f'
            

def BFS(node1, target):
    dis = [-1 for x in range(n*m)]
    dis[node1-1] = 0
    levelCount = 1
    level = levelCount // k
    l = [0]
    minWayToMohsen = math.inf
    q = [node1]
    currentNodes = [node1]
    lastKeyOfSet = node1
    while (len(q) != 0):
        t = q[0]
        q.remove(t)
        try:
            spreadFire(level, l)
            generate_nodes(level, currentNodes)
            for key in nodes[level][t]:
                if dis[key-1] == -1:
                    q.append(key)
                    dis[key-1] = dis[t-1] + 1
                if key == target:
                    if dis[key-1] < minWayToMohsen:
                        minWayToMohsen = dis[key-1]
            if t == lastKeyOfSet:
                levelCount += 1
                level = levelCount // k
            if lastKeyOfSet not in q:
                if q != []:
                    lastKeyOfSet = q[len(q) - 1]
                    currentNodes = [x for x in q]
                else:
                    lastKeyOfSet = t
                    currentNodes = [t]
        except KeyError:
            if t == lastKeyOfSet:
                levelCount += 1
                level = levelCount // k
    return minWayToMohsen

n,m,k = map(int, input().split())
park = []
fires = set()
for i in range(n):
    line = input()
    for j in range(m):
        if line[j] == 's':
            friend = [i, j]
        elif line[j] == 't':
            mohsen = [i, j]
        elif line[j] == 'f':
            fires.add((i, j))
    park.append([x for x in line])
nodes = {}
fn = friend[0] * m + friend[1] + 1
mn = mohsen[0] * m + mohsen[1] + 1
a = BFS(fn, mn)
if a == math.inf:
    a = 'Impossible'
print(a)