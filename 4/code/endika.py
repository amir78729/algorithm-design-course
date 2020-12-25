if __name__ == '__main__':
	n, k = input().split()
	n ,k = int(n), int(k)
	people = []

	input_string = input()
	input_string = [x for x in input_string]

	for level in range(n):
		empty_level = []
		empty_level.append("X")
		for vote in range(level):
			empty_level.append("X")
		people.append(empty_level)
	
	people[n-1] = input_string

	# for i in range(n - 1):
	# 	empty_level = []
	# 	for j in range(n - i - 1):
	# 		if people[n - i - 1][j] == 'K' or people[n - i - 1][j + 1] == 'K':	
	# 			empty_level.append('K')
	# 		else:
	# 			empty_level.append('B')
	# 	people[n - i - 2] = empty_level
			
	# print(people)
	remaining = k

	m = n//2
	while True:
		try:
			if people[n - 1][m] == 'B' and remaining > 0:
				people[n - 1][m] = 'K'
				remaining -= 1
				break
			else:
				m += 1
		except:
			break

	m = n//2
	while True:
		try:
			if people[n - 1][m] == 'B' and remaining > 0:
				people[n - 1][m] = 'K'
				remaining -= 1
				break
			else:
				m -= 1
		except:
			break

	
	if people[n - 1][0] == 'B':
		flag = True
	else:
		flag = False
	for index in range(n-1):
		if remaining > 0:
			if people[n - 1][index + 1] == 'B':
				if flag:
					people[n - 1][index + 1] = 'K'
					remaining -= 1
					flag = False
				else:
					flag = True
			if people[n - 1][index + 1] == 'K':
				flag = False
	
	# print(remaining)

	for last_itr in range(n):
		# print(people[n - 1][last_itr])
		if remaining > 0:
			if people[n - 1][last_itr] == 'B':
				people[n - 1][last_itr] = 'K'
				remaining -= 1
			
	for i in range(n - 1):
		empty_level = []
		for j in range(n - i - 1):
			if people[n - i - 1][j] == 'K' or people[n - i - 1][j + 1] == 'K':	
				empty_level.append('K')
			else:
				empty_level.append('B')
		people[n - i - 2] = empty_level
	
	# print(people)

	res = 0
	for p in people:
		for pp in p:
			if pp == 'K':
				res += 1
	print(res)
