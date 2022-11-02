from collections import defaultdict

def solution(clothes):
    answer = 1

    # value에 list를 담을 수 있는 dictionary 만들기
    clothes_dic = defaultdict(list)
    for cloth in clothes:
        clothes_dic[cloth[1]] += [cloth[0]]
    
    # 딕셔너리에서 key만 뽑기
    dict_keys = clothes_dic.keys()
    for key in dict_keys:
        answer *= len(clothes_dic[key]) + 1
    
    return answer - 1