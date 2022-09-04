def solution(n):
    reverse_n = sorted(str(n), reverse=True)
    answer = ('').join(reverse_n)
    return int(answer)