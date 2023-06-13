#2884
import sys

a,b=map(int,sys.stdin.readline().split())

if b<45:
    if(a>0):
        a=a-1
        b=60+(b-45)
    else:
        a=24-1
        b=60+(b-45)
else:
    b=b-45
print(a ,b)