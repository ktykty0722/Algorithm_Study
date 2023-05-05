str = input()
bomb = input()
ans = []
for s in str:
    ans.append(s)
    if s == bomb[len(bomb) - 1]:
        if len(ans) >= len(bomb):
            flag = True
            for i in range(len(bomb)):
                if bomb[i] != ans[i + (len(ans) - len(bomb))]:
                    flag = False
            if flag:
                for _ in range(len(bomb)):
                    ans.pop()

if ans:
    print(''.join(ans))
else:
    print('FRULA')
