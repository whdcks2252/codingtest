#2480
import sys

a,b,c=map(int,sys.stdin.readline().split())
d=0
if a==b and a==c:
   print(10000+a*1000)
elif a==b or a==c or b==c:
   if a==b or a==c:
    print(1000+a*100)
   elif b==c:
     print(1000+b*100)
else:
  if a>b and a>c:
    print(a*100)
  elif b>a and b>c:
    print(b*100)
  elif c>a and c>b:
    print(c*100)     