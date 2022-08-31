def solution(n):
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)
    
    for i in range(2, m+1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False
                
    result = [i for i in range(2, n+1) if sieve[i]]
    answer = len(result)
    return answer