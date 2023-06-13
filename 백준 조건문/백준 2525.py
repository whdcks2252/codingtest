#백준2525
import sys

a,b=map(int,sys.stdin.readline().split())
c=int(sys.stdin.readline())
d=b+c
while d>60 or d==60:
        a=a+1
        b=d-60
        d=d-60

if a>24 or a==24:
    a=a-24                        
b=d

print(a, b)