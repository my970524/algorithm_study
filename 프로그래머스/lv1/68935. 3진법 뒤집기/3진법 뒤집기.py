def solution(n):
    n_3 = ''
    while n > 0:
        rest = n % 3
        n = n // 3
        n_3 += str(rest)
    return int(n_3, 3)