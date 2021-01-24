def print_park(park):
    print()
    for r in range(n + 2):
        for c in range(m + 2):
            print(park[r][c], end="")
        print()

def find_fires(park, burning_ponits):
    for r in range(n + 2):
        for c in range(m + 2):
            if park[r][c] == 'f':
                f = [r,c]
                if f not in burning_ponits:
                    burning_ponits.append(f)
    return burning_ponits


def burn_point(park, burning_ponits, i, j):
    for x in range(3):
        for y in range(3):
            print(i+x-1, j+y-1)
            # try:
            #     if park[x-1+i][y-1+j] == 's' or park[x-1+i][y-1+j] == 't':
            #         return park, burning_ponits, False # someone is dead
            #     else:
            #         park[x-1+i][y-1+j] = 'f'
            #         f = ([x-1+i],[y-1+j])
            #         if f not in burning_ponits:
            #             burning_ponits.append(f)
            # except:
            #     pass
            try:
                if (park[x-1+i][y-1+j] == 's' or park[x-1+i][y-1+j] == 't'):
                    return park, burning_ponits, False # someone is dead
                else:
                    if park[x-1+i][y-1+j] == '-':
                        park[x-1+i][y-1+j] = 'f'
                        f = []
                        f.append(int([x-1+i]))
                        f.append(int([y-1+j]))
                        # f = [[x-1+i],[y-1+j]]
                        if f not in burning_ponits:
                            burning_ponits.append(f)
            except:
                pass
            
    return park, burning_ponits, True # no one is hurt

def burn(park, burning_ponits):
    for p in range(len(burning_ponits)):
        park, burning_ponits, not_done = burn_point(park, burning_ponits, burning_ponits[p][0], burning_ponits[p][1])
        if not not_done:
            return park, burning_ponits, False
    return park, burning_ponits, True

n, m, k = map(int, input().split())

park = []
tmp = []
for c in range(m + 2):
    tmp.append('x')

park.append(tmp)
for i in range(n):
    # row_input = list(map(str, input().strip().split()))[:m]
    # row_input = 'x'
    # row_input += input()
    # row_input += 'x'
    row_input = 'x' + input() + 'x'
    park.append(list(row_input))
park.append(tmp)
burning_ponits = []
burning_ponits = find_fires(park, burning_ponits)
print(burning_ponits)
park, burning_ponits, flag = burn(park, burning_ponits)


# # print(burning_ponits)
print(burning_ponits)

print_park(park)
