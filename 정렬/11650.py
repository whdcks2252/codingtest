import sys

num=int(sys.stdin.readline().strip())

arr=list()
for i in range(num):
        arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort()


for i in arr:
    for j in i:
          print(j,end=" ")
    print()