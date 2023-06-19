import sys

list1=list()
for i in range(28):
    a=int(sys.stdin.readline())
    list1.append(a)

list2=list()
for i in range(30):
    list2.append(i+1)
list3=list()
for i in list2:
    if i in  list1:
        continue
    else:
        list3.append(i)

print(min(list3))
print(max(list3))
