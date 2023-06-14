import sys

num=int(sys.stdin.readline())

list1=list(map(int,sys.stdin.readline().split()))

find=int(sys.stdin.readline())
print(list1.count(find))