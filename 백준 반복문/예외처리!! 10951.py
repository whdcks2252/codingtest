import sys

while 1:
    try:
        a,b=map(str,sys.stdin.readline().split())
        print(int(a)+int(b))
    except:
        break