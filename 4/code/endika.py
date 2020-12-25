if __name__ == '__main__':
	n, k = input().split()
	n ,k = int(n), int(k)
	people = []
	# for i in range(n):
	# 	people.append(empty)

	# print(people)
	input_string = input()
	input_string = [x for x in input_string]
	# print(input_string)
	# people.append(input_string)
	# for j in range(len(input_string)):
	# 	people[0].append(input_string[j])
# for level in range(n - 1):
# 	empty = []
# 	people.append(empty) # people[level + 1] has been created
# 	print(len(people))
# 	for j in range(n - level + 1):
# 		if people[level][j] == 'K' or people[level][j + 1] == 'K':
# 			print("k")
# 			empty.append('K')
# 		else:
# 			print("b")
# 			empty.append('B')
# 	people.append(empty)
# 	# people[2].append('l')
# 	# people[2].append('l')
# 	print(empty)
# 	print(people)
	for level in range(n):
		empty_level = []
		empty_level.append("X")
		for vote in range(level):
			empty_level.append("X")
		people.append(empty_level)
	
	people[n-1] = input_string

	

	print(people)
			
