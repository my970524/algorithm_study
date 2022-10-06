def get_score(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6
            

def solution(lottos, win_nums):
# lottos에서 0의 개수 세기
    zero_nums = lottos.count(0)
# lottos와 win_nums 비교해서 겹치는 숫자들 same_nums에 담기
    same_nums = []
    for i in lottos:
        if i in win_nums:
            same_nums.append(i)
# 최고점과 최저점 구하기
    score1 = zero_nums + len(same_nums)
    score2 = len(same_nums)
    high_score = get_score(score1)
    low_score = get_score(score2)
# 각 점수들 answer에 담기    
    answer = []
    answer.append(high_score)
    answer.append(low_score)
    return answer