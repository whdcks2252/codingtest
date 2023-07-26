import sys
import itertools

num,count=sys.stdin.readline().split()
num=int(num)
count=int(count)
arr=list()
for i in range(num):
    arr.append(i+1)

arr2=list(itertools.permutations(arr,count))

for i in arr2:
    for j in i:
         print(j,end=" ")
    print()
