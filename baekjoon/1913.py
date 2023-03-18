n = int(input())
num = int(input())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

arr = [[0 for _ in range(n)] for _ in range(n)]
direction = 0
cnt = 1
rep = 1
x, y = n // 2, n // 2
ans_y, ans_x = 0, 0
while cnt <= n ** 2:
    for _ in range(2):
        for _ in range(rep):
            if cnt <= n ** 2:
                arr[y][x] = cnt
                x += dx[direction]
                y += dy[direction]
                cnt += 1
        direction = (direction + 1) % 4
    rep += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
        if arr[i][j] == num:
            ans_y = i
            ans_x = j
    print()
print(ans_y + 1, ans_x + 1)
