from itertools import product

def solution(word):
    vowels = ['A', 'E', 'I', 'O', "U"]
    dic = []
    for i in range(1, len(vowels)+1):
        combo = product(vowels, repeat=i)
        for c in combo:
            dic.append(''.join(c))
    dic.sort()
    answer = dic.index(word) + 1
    return answer