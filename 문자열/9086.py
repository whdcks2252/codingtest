import sys 


test=int(sys.stdin.readline())

for i in range(test):
    src=list(sys.stdin.readline().rstrip())
    a=int(len(src)-1)
    print(src[0]+src[a])
    