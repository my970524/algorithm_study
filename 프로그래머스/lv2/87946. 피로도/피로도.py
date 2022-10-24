from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dungeons_list = list(permutations(dungeons, len(dungeons)))
    xp = k
    for dungeons in dungeons_list:
        explored = 0
        for dungeon in dungeons:
            if  xp>= dungeon[0]:
                xp -= dungeon[1]
                explored += 1
            else:
                break
        answer = max(answer, explored)
        xp = k
    return answer