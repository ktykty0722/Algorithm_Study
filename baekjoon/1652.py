import sys

n = int(input())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

ans = [0, 0]
for i in range(n):
    l1, l2 = 0, 0
    for j in range(n):
        if board[i][j] == '.':
            l1 += 1
        else:
            l1 = 0
        if l1 == 2:
            ans[0] += 1

        if board[j][i] == '.':
            l2 += 1
        else:
            l2 = 0
        if l2 == 2:
            ans[1] += 1

print(*ans)
