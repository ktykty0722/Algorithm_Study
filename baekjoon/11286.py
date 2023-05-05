import heapq
import sys
heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    com = int(sys.stdin.readline())
    if com == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(com), com))
