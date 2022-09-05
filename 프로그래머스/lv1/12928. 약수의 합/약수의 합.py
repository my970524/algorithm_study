def solution(n):
    answer = 0
    m = int(n ** 0.5)
    
    for i in range(1, m+1):
        if n % i == 0:
            answer += i
            if i != n // i:
                answer += n // i
    return answer
