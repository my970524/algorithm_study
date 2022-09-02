def solution(s):
    answer = 0
    if '+' in s:
        print(int(s[1:]))
        answer = int(s[1:])
    if '-' in s:
        print(int(s[1:]))
        answer = int(s[1:]) * -1
    answer = int(s)
    return answer