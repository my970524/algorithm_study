def solution(players, callings):
    answer = {}

    for i in range(len(players)):
        answer[players[i]] = i

    for call in callings:
        index = answer[call]
        back_player = players[index-1]
        players[index-1] = call
        players[index] = back_player
        answer[call] -= 1
        answer[back_player] += 1
        
    return players