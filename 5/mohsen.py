def print_park():
    print()
    for r in range(n + 2):
        for c in range(m + 2):

            if park[r][c] != 'x':
                print(park[r][c], end="")

            # print(park[r][c], end="")

        print()

###############################################################################
# FIRE RELATED FUNCTIONS

def find_fires(): # save 'f' cells in the matrix
    for r in range(n + 2):
        for c in range(m + 2):
            if park[r][c] == 'f':
                f = [r,c]
                if f not in burning_ponits:
                    burning_ponits.append(f)


def burn_point( i, j): 
    for x in range(3):
        for y in range(3):
            try:
                # if (park[x-1+i][y-1+j] == 's' or park[x-1+i][y-1+j] == 't'):
                if park[x-1+i][y-1+j] == 't':
                    return False # someone is dead
                else:
                    if park[x-1+i][y-1+j] == '-' or park[x-1+i][y-1+j] == 's' :
                        park[x-1+i][y-1+j] = 'f'
                        f = []
                        f.append(int([x-1+i]))
                        f.append(int([y-1+j]))
                        # f = [[x-1+i],[y-1+j]]
                        if f not in burning_ponits:
                            burning_ponits.append(f)
                        s_ponits.remove(f)
            except:
                pass
    return True # no one is hurt

def burn():
    global burning_ponits
    for p in range(len(burning_ponits)):
        not_done = burn_point(burning_ponits[p][0], burning_ponits[p][1])
        if not not_done:
            return False
    return True

###############################################################################
# WALKING RELATED FUNCTIONS

def find_s(): # save 'f' cells in the matrix
    for r in range(n + 2):
        for c in range(m + 2):
            if park[r][c] == 's':
                s = [r,c]
                if s not in s_ponits:
                    s_ponits.append(s)


def walk_from_point( i, j): 
    try:
        # if (park[x-1+i][y-1+j] == 's' or park[x-1+i][y-1+j] == 't'):
        x, y = i, j + 1
        if park[x][y] == 't':
            return True # Mohsen is here
        else:
            if park[x][y] == '-':
                park[x][y] = 's'
                f = []
                f.append(int([x]))
                f.append(int([y]))
                # f = [[x-1+i],[y-1+j]]
                if f not in s_ponits:
                    s_ponits.append(f)
    except:
        pass

    try:
        # if (park[x-1+i][y-1+j] == 's' or park[x-1+i][y-1+j] == 't'):
        x, y = i, j - 1
        if park[x][y] == 't':
            return True # Mohsen is here
        else:
            if park[x][y] == '-':
                park[x][y] = 's'
                f = []
                f.append(int([x]))
                f.append(int([y]))
                # f = [[x-1+i],[y-1+j]]
                if f not in s_ponits:
                    s_ponits.append(f)
    except:
        pass

    try:
        # if (park[x-1+i][y-1+j] == 's' or park[x-1+i][y-1+j] == 't'):
        x, y = i + 1, j
        if park[x][y] == 't':
            return True # Mohsen is here
        else:
            if park[x][y] == '-':
                park[x][y] = 's'
                f = []
                f.append(int([x]))
                f.append(int([y]))
                # f = [[x-1+i],[y-1+j]]
                if f not in s_ponits:
                    s_ponits.append(f)
    except:
        pass

    try:
        # if (park[x-1+i][y-1+j] == 's' or park[x-1+i][y-1+j] == 't'):
        x, y = i - 1, j 
        if park[x][y] == 't':
            return True # Mohsen is here
        else:
            if park[x][y] == '-':
                park[x][y] = 's'
                f = []
                f.append(int([x]))
                f.append(int([y]))
                # f = [[x-1+i],[y-1+j]]
                if f not in s_ponits:
                    s_ponits.append(f)
    except:
        pass


    return False # We have not found him yet

def walk():
    global s_ponits
    for p in range(len(s_ponits)):
        not_done = walk_from_point(s_ponits[p][0], s_ponits[p][1])
        if not_done:
            return False
    return True

###############################################################################

n, m, k = map(int, input().split())

park = []
tmp = []
for c in range(m + 2):
    tmp.append('x')

park.append(tmp)
for i in range(n):
    row_input = 'x' + input() + 'x'
    park.append(list(row_input))
park.append(tmp)
burning_ponits = []
s_ponits = []
# print(burning_ponits)
time = 0
is_impossible = False
while True:
    time += 1
    # print(time)
    
    if time % k == 0:
        find_fires()
        # flag = burn()
        if not burn():
            is_impossible = True
            break
    find_s()
    # s_flag = walk()
    if not walk() :
        break

    
    # print_park()
if is_impossible:
    print("Impossible")
else:
    print(time)


# print(burning_ponits)
# print_park()

# find_fires()
# flag = burn()
# print(burning_ponits)
# print_park()
