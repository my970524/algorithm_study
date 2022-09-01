def solution(s):
    my_list = s.split(' ')
    my_list2 = []
    for i in my_list:
        word = ''
        for j in range(len(i)):
            if j % 2 == 0:
                word += i[j].upper()
            else:
                word += i[j].lower()
        my_list2.append(word)
    answer = (' ').join(my_list2)
    return answer