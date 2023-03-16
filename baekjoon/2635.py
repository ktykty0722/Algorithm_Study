n = int(input())
ans = []

for i in range(n + 1):
    temp = [n, i]
    j = 0
    while True:
        next_num = temp[j] - temp[j + 1]
        if next_num >= 0:
            temp.append(next_num)
        else:
            break
        j += 1
    if len(ans) < len(temp):
        ans = temp

print(len(ans))
print(*ans)
