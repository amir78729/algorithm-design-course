def knap_sack(backpack, weight, value, n): 
	if n == 0 or backpack == 0: 
		return 0
	if (weight[n-1] > backpack): 
		return knap_sack(backpack, weight, value, n-1) 
	else: 
		return max( 
			value[n-1] + knap_sack( 
				backpack-weight[n-1], weight, value, n-1), 
			knap_sack(backpack, weight, value, n-1)) 

if __name__ == '__main__':
    t = input()
    n, backpack = input().split()
    n, backpack = int(n), int(backpack)
    value = [] 
    weight = [] 
    for i in range(n):
        w, v = input().split()
        value.append(int(v))
        weight.append(int(w))
    
    # backpack = 50
    # n = len(value) 
    print( knap_sack(backpack, weight, value, n) )