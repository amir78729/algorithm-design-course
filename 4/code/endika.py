import ctypes
from ctypes import c_longlong as ll

n, K = map(int,input().split())
s = input()
maxn = 510
arr = [[[63 for k in range(maxn)] for j in range(maxn)] for i in range(2)]
# string t;
cur = 0
prv = 1
# ctypes.memset(arr[cur], 63,  len(arr[cur]));

# arr = [[63 for k in range(maxn)] for j in range(maxn)] 

# arr[cur][0][0] = 0;
for i in range(n) :
	cur, prv = prv, cur
	# ctypes.memset(arr[cur], 63, len(arr[cur]) )

	# arr = [[63 for k in range(maxn)] for j in range(maxn)] 

	for j in range(i) :
	# for (int j = 0; j <= i + 1; j++) :
		for k in range(K):
		# for (int k = 0; k <= K; k++) :
			# //don't change!
			if s[i] == 'B' and j:
				arr[cur][j][k] = min(arr[cur][j][k], arr[prv][j - 1][k] + j)
			elif s[i] == 'K':
				arr[cur][0][k] =min(arr[cur][0][k], arr[prv][j][k])
			# //change
			if s[i] == 'K':
				continue;
			if k:
				arr[cur][0][k]= min(arr[cur][0][k], arr[prv][j][k - 1])
			

# print(arr)	

# LL ans = 1e18;
ans = 10000000000000000000000000000000
for j in range(n):
	for k in range(K):
		ans=min(ans, arr[cur][j][k])
print(int(len(ll()) *  n * (n + 1) / 2 - ans)) 
print(ans)
# return 0;
