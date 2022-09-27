from collections import deque

def solution(maps):
    limit_x = len(maps)
    limit_y = len(maps[0])
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            
            if 0 <= n_x < limit_x and 0 <= n_y < limit_y and maps[n_x][n_y] == 1:
                maps[n_x][n_y] = maps[x][y] + 1
                queue.append((n_x, n_y))
    print(maps)
    if maps[-1][-1] > 1:
        return maps[-1][-1]
    return -1

