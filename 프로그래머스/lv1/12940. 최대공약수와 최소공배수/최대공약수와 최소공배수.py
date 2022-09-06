def greatest_common_division(n, m):
    while m > 0:
        n, m = m, n % m
    return n

def solution(n, m):
    gcd = greatest_common_division(n, m)
    lcm = n * m // gcd
    answer = [gcd, lcm]
    return answer