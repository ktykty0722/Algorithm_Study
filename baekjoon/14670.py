n = int(input())
medi = {}
for _ in range(n):
    n1, n2 = map(int, input().split())
    medi[n1] = n2

r = int(input())
for _ in range(r):
    ans = []
    l = list(map(int, input().split()))
    for i in range(l[0]):
        if l[i + 1] in medi.keys():
            ans.append(medi.get(l[i + 1]))

    if len(ans) == len(l) - 1:
        print(*ans)
    else:
        print('YOU DIED')
