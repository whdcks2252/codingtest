import sys

num=9

list1=list()
for i in range(num):
    list1.append(int(sys.stdin.readline()))

result=max(list1)
print(result)
print(list1.index(result)+1)
