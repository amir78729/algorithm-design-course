def select_activities( ): 
	global res
	i = 0
	for j in range(k): 
		if s[j][0] >= s[i][1]: 
			res += 1
			i = j 
            
def takeSecond(elem):
    return elem[1]

if __name__ == '__main__':

    s = [] 
    f = [] 
    res = 0
    n, k = input().split()
    n, k = int(n),int(k)
    for index in range(k):
        l, r = input().split()
        tmp = []
        s.append(tmp)
        s[index].append(int(l))
        s[index].append(int(r))
    s.sort(key=takeSecond)
    if n <= k and n != 0:
        select_activities()
        print("YES")
        # if res >= n: 
            # print("YES")
        # else:
        #     print("NO")
    else:
        print("NO")
