N = int(input())

graph = []
for _ in range(N):
  graph.append(list(map(int, input())))

count = 0

def dfs(x, y):
  if not 0<= x < N or not 0 <= y < N:
    return False

  if graph[x][y] == 1:
    global count
    graph[x][y] = 0
    count += 1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
    
result = []

for i in range(N):
  for j in range(N):
    if dfs(i, j) == True:
      result.append(count)
      count = 0

result.sort()
print(len(result))
for i in result:
  print(i)