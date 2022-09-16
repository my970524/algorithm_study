def solution(answers):
    answer = []
    num = len(answers)
    
    p_1 = [1,2,3,4,5] * num
    p_2 = [2,1,2,3,2,4,2,5] * num
    p_3 = [3,3,1,1,2,2,4,4,5,5] * num

    scores = {1:0, 2:0, 3:0}
    
    for i in range(num):
        if answers[i] == p_1[i]:
            scores[1] += 1
    for i in range(num):
        if answers[i] == p_2[i]:
            scores[2] += 1
    for i in range(num):
        if answers[i] == p_3[i]:
            scores[3] += 1

    max_score = max(scores.values())

    for i in range(1, 4):
        if scores[i] == max_score:
            answer.append(i)
    return answer