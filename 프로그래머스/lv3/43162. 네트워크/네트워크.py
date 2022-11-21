from collections import deque

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        visited[v-1] = True
        for i in graph[v]:
            if visited[i-1] == False:
                queue.append(i)
    return visited

def solution(n, computers):
    answer = 0
    visited = [False] * n
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i+1].append(j+1)

    true_num = 0
    for i in range(1, n+1):
        bfs_result = bfs(graph, i, visited)
        if bfs_result.count(True) > true_num:
            true_num = bfs_result.count(True)
            answer += 1

    return answer