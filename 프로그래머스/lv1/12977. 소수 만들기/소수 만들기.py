from itertools import combinations

def check_prime(n):
    m = int(n**0.5)
    
    for i in range(2, m+1):
        if n % i == 0:
            return False
    return True
        
def solution(nums):
    answer = 0
    comb = list(combinations((nums), 3))
    candidate = []
    for c in comb:
        candidate.append(sum(c))
    for c in candidate:
        if check_prime(c):
            answer += 1
    return answer