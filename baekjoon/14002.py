import sys
from bisect import bisect_left

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

lis = [arr[0]]

for a in arr:
    if lis[-1] < a:
        lis.append(a)
    else:
        idx = bisect_left(lis, a)
        lis[idx] = a

print(len(lis))
print(*lis)