import heapq
import sys

n = int(sys.stdin.readline().rstrip())
heap1 = []
heap2 = []
ans = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if len(heap1) == len(heap2):
        heapq.heappush(heap1, -num)
    else:
        heapq.heappush(heap2, num)

    if heap2 and -heap1[0] > heap2[0]:
        left = heapq.heappop(heap1)
        right = heapq.heappop(heap2)

        heapq.heappush(heap1, -right)
        heapq.heappush(heap2, -left)

    print(-heap1[0])

