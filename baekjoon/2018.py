n = int(input())
ans, cnt = 0, 0
st, en = 0, 0

while en <= n:
    if ans < n:
        en += 1
        ans += en
    elif ans > n:
        ans -= st
        st += 1
    else:
        cnt += 1
        en += 1
        ans += en

print(cnt)
