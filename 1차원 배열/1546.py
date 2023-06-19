import sys

n=int(sys.stdin.readline())

list1=list(map(int,sys.stdin.readline().split()))

ma=max(list1)
av=0
for i in range(n):
    av+=list1[i]/ma*100

print(av/n)   