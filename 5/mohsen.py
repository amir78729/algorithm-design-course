n, m, k = map(int, input().split())

park = []

for i in range(n):
    # row_input = list(map(str, input().strip().split()))[:m]
    row_input = input()
    park.append(row_input)

print(park)