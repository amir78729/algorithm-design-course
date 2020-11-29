import time
comparisons = 0

def merge(index, l, r, ):
    i = j = k = 0
    while i < len(l) and j < len(r):
        if len(l[i]) > index and len(r[j]) > index:
            if ord(l[i][index]) <= ord(r[j][index]):
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
        else:
            if len(l[i]) < len(r[j]):
                arr[k] = l[i]
                i += 1
            elif len(l[i]) > len(r[j]):
                arr[k] = r[j]
                j += 1
            elif len(l[i]) == len(r[j]):
                arr[k] = l[i]
                i += 1
            comparisons += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1


def merge_sort(arr, index):
    global comparisons
    # recursive part:
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        merge_sort(l, index)
        merge_sort(r, index)
        merge(index,l,r)
        # i = j = k = 0

        # merging:
        # while i < len(l) and j < len(r):
        #     if len(l[i]) > index and len(r[j]) > index:
        #         if ord(l[i][index]) <= ord(r[j][index]):
        #             arr[k] = l[i]
        #             i += 1
        #         else:
        #             arr[k] = r[j]
        #             j += 1
        #     else:
        #         if len(l[i]) < len(r[j]):
        #             arr[k] = l[i]
        #             i += 1
        #         elif len(l[i]) > len(r[j]):
        #             arr[k] = r[j]
        #             j += 1
        #         elif len(l[i]) == len(r[j]):
        #             arr[k] = l[i]
        #             i += 1
        #         comparisons += 1
        #     k += 1

        # while i < len(l):
        #     arr[k] = l[i]
        #     i += 1
        #     k += 1
        # while j < len(r):
        #     arr[k] = r[j]
        #     j += 1
        #     k += 1


def radix_sort(arr, m):
    for i in (range(m)):
        merge_sort(arr, i)
        print(*arr)


array = []
mx = 0
n = int(input())
for i in range(n):
    s = input()
    array.append(s)
    if len(s) > mx:
        mx = len(s)
radix_sort(array, mx)

# array = []
# mx = 0
# myfile = open('input11.txt', 'r')
# lines = myfile.readlines()
# print(lines)
# n = int(lines[0])
# print(n)
# for i in range(1, n+1):
#     line = lines[i].rstrip()
#     array.append(line)
#     if len(line) > mx:
#         mx = len(line)

    # print(array)
# print(mx)
# print(array)
# start_time = time.time()
# merge_sort(array, mx)
# print("----%s seconds ----" % (time.time() - start_time))
# print(comparisons)