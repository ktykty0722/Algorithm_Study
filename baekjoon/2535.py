n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[2], reverse=True)
ans_con = []
ans = []
for i in range(n):
    if ans_con.count(arr[i][0]) < 2:
        ans.append([arr[i][0], arr[i][1]])
        ans_con.append(arr[i][0])
    if len(ans) == 3:
        break

for i in ans:
    print(i[0], i[1])
