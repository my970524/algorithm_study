from itertools import permutations

def check_decimal(num):
    if num == 0 or num == 1:
        return False
    m = int(num ** 0.5)
    for i in range(2, m+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    answer = 0
    n = len(numbers)
    candidates = []

    for i in range(1, n+1):
        combo = list(permutations(numbers, i))
        for c in combo:
            c = ('').join(c)
            candidates.append(int(c))

    candidates = set(candidates)
    
    for candidate in candidates:
        if check_decimal(candidate):
            answer += 1
    return answer