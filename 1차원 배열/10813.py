import sys

n,m=map(int,sys.stdin.readline().split())
list1=list()
for i in range(n):
    list1.append(i+1)

temp1=0
for i in range(m):
    i,j=map(int,sys.stdin.readline().split())
  
    temp=list1[i-1]
    list1[i-1]=list1[j-1]
    list1[j-1]=temp


for i in list1:
    print(i,end=" ")
