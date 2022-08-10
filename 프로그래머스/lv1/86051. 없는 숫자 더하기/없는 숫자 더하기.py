num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def solution(numbers):
    answer = 0
    for i in num:
        if i not in numbers:
            answer += i
    return answer

# 다른 사람의 풀이
def solution(numbers):
    '''
    numbers에는 0~9까지의 숫자 중 일부가 빠져있고, 빠진 숫자들의 합을 구하는 문제
    => 0~9까지의 합 - numbers에 있는 숫자들의 합
    '''
    return 45 - sum(numbers)
