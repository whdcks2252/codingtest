##이진탐색
import sys
import bisect

N = int(sys.stdin.readline().strip())
card = list(map(int, input().split()))
M = int(sys.stdin.readline().strip())
other=list(map(int,sys.stdin.readline().split()))
card.sort()

for o in other:
    l = bisect.bisect_left(card, o) #o의 인덱스 반환
    r = bisect.bisect_right(card, o) #o의 인덱스+1반환
    print(r - l, end=' ')



##이 예제는 정렬된 값이 몇개 있는지 
