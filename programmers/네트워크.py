def solution(n, computers):
    answer = 0
    arr = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                arr[i].append(j)

    for x in range(n):
        if not visited[x]:
            q = [x]
            visited[x] = True
            while q:
                now = q.pop()
                for next in arr[now]:
                    if not visited[next]:
                        q.append(next)
                        visited[next] = True
            answer += 1
    return answer
