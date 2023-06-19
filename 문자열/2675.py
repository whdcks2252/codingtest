import sys

t=int(sys.stdin.readline())

list3=list()
for i in range(t):
    list1=list()
    n,s=map(str,sys.stdin.readline().split())
    n=int(n)
    list2=list(s)
    for j in range(len(list2)):
        d=list2[j]*n
        list1.append(d)
    s=""
    for p in range(len(list1)):
        s+=list1[p]
    list3.append(s)
    

for i in list3:    
    print(i)
