import sys

list1=list()
for i in range(10):
    num=int(sys.stdin.readline())
    list1.append(num%42)


list2=list()
for i in list1:
    if i in list2:
        continue
    else:
        list2.append(i)

print(len(list2))