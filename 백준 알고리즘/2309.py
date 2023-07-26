import sys
import itertools

arr=list()

for i in range(9):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()

nc=itertools.combinations(arr,7)
arr2=list(nc)

for i in arr2:
    if sum(i)==100:
        d=list(i)
        for j in range(7):
            print(d[j])
        break
    

