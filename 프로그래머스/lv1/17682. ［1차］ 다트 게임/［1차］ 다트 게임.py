def solution(dartResult):
    score = list(map(str, [i for i in range(10)]))
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = ['*', '#']
    round_score = []
    for i in range(len(dartResult)):
        if dartResult[i] in score:
            if dartResult[i+1] in score:
                round_score.append(int(dartResult[i:i+2]))
            elif dartResult[i-1] in score:
                pass
            else:
                round_score.append(int(dartResult[i]))
        elif dartResult[i] in bonus:
            round_score[-1] = round_score[-1] ** bonus[dartResult[i]]
        elif dartResult[i] in option:
            if dartResult[i] == '*':
                if len(round_score) > 1:
                    round_score[-1] = round_score[-1] * 2
                    round_score[-2] = round_score[-2] * 2
                else:
                    round_score[-1] = round_score[-1] * 2
            elif dartResult[i] == '#':
                round_score[-1] = round_score[-1] * -1
    return sum(round_score)