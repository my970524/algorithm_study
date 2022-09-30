import copy

limit_y, limit_x = map(int, input().split())

bg1 = []
for _ in range(limit_x):
  bg1.append(list(input()))

bg2 = copy.deepcopy(bg1)

power = 0

def dfs(x, y, bg, side1, side2):
  global power
  if not 0 <= x < limit_x or not 0 <= y < limit_y:
    return power

  if bg[x][y] == side1:
    bg[x][y] = side2 
    power += 1

    dfs(x-1, y, bg, side1, side2)
    dfs(x, y-1, bg, side1, side2)
    dfs(x+1, y, bg, side1, side2)
    dfs(x, y+1, bg, side1, side2)

    return power 
  return power 

result1 = 0
result2 = 0

for i in range(limit_x):
  for j in range(limit_y):
    result1 += dfs(i, j, bg1, 'W', 'B') ** 2
    power = 0
for i in range(limit_x):
  for j in range(limit_y):
    result2 += dfs(i, j, bg2, 'B', 'W') ** 2
    power = 0

print(result1, result2)