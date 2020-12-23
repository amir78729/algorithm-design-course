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
    value = [60, 100, 120] 
    weight = [10, 20, 30] 
    backpack = 50
    n = len(value) 
    print( knap_sack(backpack, weight, value, n) )

