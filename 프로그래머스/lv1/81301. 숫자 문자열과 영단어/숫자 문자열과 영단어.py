numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
number_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

def solution(s):
    answer = ''
    en = ''
    
    for i in s:
        if i in numbers:
            answer += i
        else:
            en += i
            if en in number_dic:
                answer += number_dic[en]
                en = ''
    return int(answer)