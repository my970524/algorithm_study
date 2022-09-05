def solution(n):
    answer = 0
    m = int(n ** 0.5)
    if m ** 2 != n:
        return -1
    return (m+1) ** 2