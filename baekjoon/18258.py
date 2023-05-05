from collections import deque
import sys
q = deque()
for _ in range(int(sys.stdin.readline())):
    com = list(sys.stdin.readline().rstrip().split(' '))
    if com[0] == 'push':
        q.append(int(com[1]))
    elif com[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(q))
    elif com[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)

    elif com[0] == 'back':
        if q:
            print(q[len(q)-1])
        else:
            print(-1)
