import sys
left = list(sys.stdin.readline().rstrip())
right = []
n = int(input())
for _ in range(n):
    com = sys.stdin.readline()
    if com[0] == 'L':
        if left:
            right.append(left.pop())
    elif com[0] == 'D':
        if right:
            left.append(right.pop())
    elif com[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(com[2])
left.extend(reversed(right))
print(''.join(left))
