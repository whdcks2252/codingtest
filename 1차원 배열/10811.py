import sys

n,m=map(int,sys.stdin.readline().split())
list1=list()
for i in range(n):
    list1.append(i+1)


for i in range(m):    
    j,k=map(int,sys.stdin.readline().split())
    
    list2=list(list1[j-1:k])
    list2.reverse()
    p=0
    for d in range(j-1,k):
            list1[d]=list2[p]
            p+=1


for i in list1:
    print(i,end=" ")
