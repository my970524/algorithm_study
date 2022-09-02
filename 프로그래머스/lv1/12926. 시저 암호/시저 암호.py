def solution(s, n):
    answer = ''
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in s:
        # i가 공백이면 그대로
        if i == ' ':
            answer += i
        # i가 대문자이면
        elif i.isupper():
            new_i = alph[alph.index(i.lower()) + n - 26].upper()
            answer += new_i
        # i가 소문자이면
        else:
            new_i = alph[alph.index(i) + n -26]
            answer += new_i
    return answer