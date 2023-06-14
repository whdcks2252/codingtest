import sys

a,b=map(int,sys.stdin.readline().split())

list1=list(map(int,sys.stdin.readline().split()))
list2=list()
for i in list1:
    if i<b:
        list2.append(i)

for i in list2:
    print(i,end=" ")