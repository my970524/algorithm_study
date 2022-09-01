def solution(n):
    answer = '수'
    for i in range(n - 1):
        if answer[-1] == '수':
            answer += '박'
        else:
            answer += '수'
    return answer