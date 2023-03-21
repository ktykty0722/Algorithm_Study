n, m, y, x, k = map(int, input().split())
dice = [0 for _ in range(6)]
arr = []
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
for _ in range(n):
    arr.append(list(map(int, input().split())))
order = list(map(int, input().split()))

for i in order:
    ny = y + dy[i - 1]
    nx = x + dx[i - 1]
    if 0 <= ny < n and 0 <= nx < m:
        if i == 1:
            dice[0], dice[5], dice[2], dice[4] = dice[5], dice[2], dice[4], dice[0]
        elif i == 2:
            dice[0], dice[4], dice[2], dice[5] = dice[4], dice[2], dice[5], dice[0]
        elif i == 3:
            dice[0], dice[3], dice[2], dice[1] = dice[3], dice[2], dice[1], dice[0]
        elif i == 4:
            dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
        if arr[ny][nx] != 0:
            dice[2] = arr[ny][nx]
            arr[ny][nx] = 0
        else:
            arr[ny][nx] = dice[2]
        y = ny
        x = nx
        print(dice[0])
