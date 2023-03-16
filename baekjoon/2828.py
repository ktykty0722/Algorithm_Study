n, m = map(int, input().split())
j = int(input())
now = 1
ans = 0
for _ in range(j):
    num = int(input())
    if now > num:
        move = num
        ans += now - move
        now = move
    elif num > (now + m - 1):
        move = num - m + 1
        ans += move - now
        now = move

print(ans)
