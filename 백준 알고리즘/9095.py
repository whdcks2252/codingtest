import sys
def f(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    if(n==4):
        return 1+2+4
    return f(n-1)+f(n-2)+f(n-3)
    
#dp 알고리즘 +  재귀함수
    
num=int(sys.stdin.readline().strip())
arr=list()
for i in range(num):
    arr.append(int(sys.stdin.readline().strip()))


for i in arr:
    if i==1:
        print(int(1))
    elif i==2:
        print(int(2))
    elif i==3:
        print(int(4))
    else:
       print(f(i))



