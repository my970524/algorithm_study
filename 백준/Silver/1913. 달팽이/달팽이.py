n = int(input())
target = int(input())

mat = [[0 for _ in range(n)] for _ in range(n)]

start_num = n ** 2

if target == start_num:
    target_position = [0, 0]
else:
    target_position = []

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
cur_direction = directions[0]

position = [0, 0]
mat[0][0] = start_num

for i in range(start_num, 1, -1):
    possible_direction = []
    for j in range(len(directions)):
        next_position = [x+y for x,y in zip(position, directions[j])]

        a, b = next_position
        if a < 0 or a >= n or b < 0 or b >= n:
            pass
        else:
            next_position_value = mat[a][b]

            if next_position_value > 0:
                pass
            else:
                possible_direction.append(directions[j])

    if len(possible_direction) > 1:
        cur_direction = cur_direction
    else:
        cur_direction = possible_direction[0]

    position = [x+y for x,y in zip(position, cur_direction)]

    x, y = position

    mat[x][y] = i -1

    if mat[x][y] == target:
        target_position = [x, y]

for i in range(len(mat)):
    values = (' ').join(map(str, mat[i]))
    print(values)

x, y = target_position
print(x+1, y+1)