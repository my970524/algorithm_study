def minus_one(num):
    return num-1

def solution(board, moves):
    answer = 0
    # 리스트 인덱스 맞추기 위해 moves의 요소들 -1
    moves = list(map(minus_one, moves))

    # 꺼낸 인형들
    out = []

    for y in moves:
        for x in range(len(board)):
            if board[x][y] != 0:
                out.append(board[x][y])
                board[x][y] = 0
                if len(out) > 1 and out[-1] == out[-2]:
                    del out[-2:]
                    answer += 2
                break
            
    return answer