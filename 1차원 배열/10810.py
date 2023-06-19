import sys

n,m=map(int,sys.stdin.readline().split())
list1=list()
for i in range(n):
    list1.append(0)

for i in range(m):
    i,j,k=map(int,sys.stdin.readline().split())
    for l in range(i-1,j):
        list1[l]=k

for i in list1:
    print(i,end=" ")