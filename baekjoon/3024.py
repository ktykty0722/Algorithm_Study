n = int(input())
arr = [input() for _ in range(n)]
if n < 3:
    print('ongoing')
    exit()
for i in range(n - 2):
    for j in range(n - 2):
        if arr[i][j] != '.':
            if arr[i][j] == arr[i + 1][j + 1] == arr[i + 2][j + 2]:
                print(arr[i][j])
                exit()
for i in range(n - 2):
    for j in range(n - 2):

        if arr[i][n - j - 1] != '.':
            if arr[i][n - j - 1] == arr[i + 1][n - (j + 1) - 1] == arr[i + 2][n - (j + 2) - 1]:
                print(arr[i][n - j - 1])
                exit()

for i in range(n - 2):
    for j in range(n):
        if arr[i][j] != '.':
            if arr[i][j] == arr[i + 1][j] == arr[i + 2][j]:
                print(arr[i][j])
                exit()

for i in range(n):
    for j in range(n - 2):
        if arr[i][j] != '.':
            if arr[i][j] == arr[i][j + 1] == arr[i][j + 2]:
                print(arr[i][j])
                exit()

print('ongoing')
