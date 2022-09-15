def solution(survey, choices):
    # 각 지표에 대한 점수 초기화
    score = {'R': 0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    answer = ''
    
    for i in range(len(choices)):
        # choices에서 비동의에 해당하는 범위라면,
        if 1 <= choices[i] <= 3:
            # survey[i][0] 캐릭터가 비동의 선택 유형이므로 
            # score[survey[i][0]] 의 점수를 더해줌
            score[survey[i][0]] += 4 - choices[i]
        
        # choices에서 동의에 해당하는 범위라면,
        elif 5 <= choices[i] <= 7:
            # survey[i][0] 캐릭터가 동의 선택 유형이므로
            # score[survey[i][1]] 의 점수를 더해줌
            score[survey[i][1]] += choices[i] - 4
        else:
            # choices에서 모르겠음을 선택했으므로, 점수 변화 없음
            pass
    # 각 항목에 대해 값 비교해서 answer에 추가
    if score['R'] >= score['T']:
        answer += 'R'
    else:
        answer += 'T'
    if score['C'] >= score['F']:
        answer += 'C'
    else:
        answer += 'F'
    if score['J'] >= score['M']:
        answer += 'J'
    else:
        answer += 'M'
    if score['A'] >= score['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer