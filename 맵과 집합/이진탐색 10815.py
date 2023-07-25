##이진탐색
import sys
import bisect

N = int(sys.stdin.readline().strip())
card = list(map(int, input().split()))
M = int(sys.stdin.readline().strip())
other=list(map(int,sys.stdin.readline().split()))
card.sort()

for o in other:
    l = bisect.bisect_left(card, o)
    r = bisect.bisect_right(card, o)
    print(r - l, end=' ')

