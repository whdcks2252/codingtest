import sys



num,mx=sys.stdin.readline().split()
num=int(num)
mx=int(mx)
arr=list(map(int,sys.stdin.readline().split()))
result= 0

for i in range(num):
    for j in range(i+1,num):
        for k in range(j+1,num):
            if arr[i]+arr[j]+arr[k]>mx:
                continue
            else:
                result=max(result,arr[i]+arr[j]+arr[k])

print(result)