def solution(strings, n):
    answer = []
    order_dic = {}
    strings = sorted(strings)
    
    for string in strings:
        order_dic[string] = string[n]
    ordered_strings = sorted(order_dic.items(), key=lambda item: item[1])
    
    for string in ordered_strings:
        answer.append(string[0])
    return answer