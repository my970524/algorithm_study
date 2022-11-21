from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    graph[n1].sort()
    graph[n2].sort()

dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

def dfs(v):
    dfs_visited[v] = True
    print(v, end=' ')

    for node in graph[v]:
        if dfs_visited[node] == False:
            dfs(node)

def bfs(v):
    queue = deque()
    queue.append(v)
    bfs_visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for node in graph[v]:
            if bfs_visited[node] == False:
                queue.append(node)
                bfs_visited[node] = True

dfs(V)
print()
bfs(V)