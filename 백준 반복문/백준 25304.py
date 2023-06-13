import sys

price=int(sys.stdin.readline())

num=int(sys.stdin.readline())
sum=0
for i in range(num):
    a,b=map(int,sys.stdin.readline().split())
    sum=sum+(a*b)
if price==sum:
    print("Yes")
else:
    print("No")