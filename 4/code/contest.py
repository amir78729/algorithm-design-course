# def select_activities( ): 
# 	global res
    
# 	i = 0
# 	for j in range(1,len(s)): 
#         #  if(questions[i].r >= questions[i-1].l  || (questions[i].l >= questions[i-1].r && questions[i].r >= questions[i-1].r))
# 		if  (s[j][1] >= s[j-1][0] or (s[j][0] >= s[j-1][1] and s[j][1] >= s[j-1][1])): 
# 			# if res != n-1:
# 			res += 1
# 			# i = j 
# 		# if s[j][0] >= s[i][1]: 
# 		# 	res0 += 1
# 		# 	i = j 
            
# def takeSecond(elem):
#     return elem[1]

# if __name__ == '__main__':
#     s = [] 
#     res = 1
#     res0 = 0
#     n, k = input().split()
#     n, k = int(n),int(k)
#     for index in range(k):
#         l, r = input().split()
#         tmp = []
#         s.append(tmp)
#         s[index].append(int(l))
#         s[index].append(int(r))
#     s.sort(key=takeSecond)
    
#     # if 0 < n <= k and n != 0:
#     # if 0 < len(s) <= k:
#     #     select_activities()
#     #     # print("YES")
#     #     if res >= n: 
#     #         print("YES")
#     #     else:
#     #         print("NO")
#     # else:
#     #     print("NO")الان
#     # print("NO")
#     if len(s) < k :
#         print("NO")
#     else:
#         s.sort(key=takeSecond)
#         select_activities()
#         if res > n : 
#             print("YES")
#         else:
#             print("NO")


# ###############################################

class Q:
	def __init__(self, l, r):
		self.l=l
		self.r=r

def bs(s):
	n = len(s)
	for i in range(n):
		for j in range(n - 1):
			if s[j].l > s[j+1].r :
				t = s[j];
				s[j] = s[j + 1];
				s[j + 1] = t;
	return s

def select_activities(s,k,n ): 
	if len(s) < k :
		print("NO")
		return
	res = 1
	s = bs(s)
	for i in range(1,len(s)): 
		if(s[i].r >= s[i-1].l  or (s[i].l >= s[i-1].r and s[i].r >= s[i-1].r)):
			res += 1
	if res >= n : 
		print("YES")
	else:
		print("NO")

if __name__ == '__main__':
	s = [] 
	n, k = input().split()
	n, k = int(n),int(k)
	for index in range(k):
		l, r = input().split()
		l, r = int(l),int(r)
		tmp = Q(l,r)
		s.append(tmp)
	select_activities(s, k, n)
    


# ###############################################

# def select_activities( ): 
# 	global res
    
# 	# i = 0
# 	for j in range(1,len(s)): 
#         #  if(questions[i].r >= questions[i-1].l  || (questions[i].l >= questions[i-1].r && questions[i].r >= questions[i-1].r))
# 		if  s[j][1] >= s[j-1][0] or (s[j][0] >= s[j-1][1] and s[j][1] >= s[j-1][1]): 
# 			if res == n-1 and j == len(s)-1:
# 				pass
# 			else:
# 				res += 1
# 			# i = j 
            
# def takeSecond(elem):
#     return elem[1]

# if __name__ == '__main__':
#     s = [] 
#     res = 1
#     n, k = input().split()
#     n, k = int(n),int(k)
#     for index in range(k):
#         l, r = input().split()
#         tmp = []
#         s.append(tmp)
#         s[index].append(int(l))
#         s[index].append(int(r))
#     s.sort(key=takeSecond)
    
#     # if 0 < n <= k and n != 0:
#     # if 0 < len(s) <= k:
#     #     select_activities()
#     #     # print("YES")
#     #     if res >= n: 
#     #         print("YES")
#     #     else:
#     #         print("NO")
#     # else:
#     #     print("NO")

#     if len(s) < k or n > k :
#         print("NO")
#     else:
#         s.sort(key=takeSecond)
#         select_activities()
#         # print("YES")
#         if res >= n: 
#             print("YES")
#         else:
#             print("NO")
