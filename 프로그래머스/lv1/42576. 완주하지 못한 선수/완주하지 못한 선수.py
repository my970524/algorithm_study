def solution(participant, completion):
    answer = ''
    my_dict = dict.fromkeys(participant, 0)
    
    for i in participant:
        my_dict[i] += 1
    
    for i in completion:
        my_dict[i] -= 1
    
    for key, value in my_dict.items():
        if value != 0:
            answer = key
            
    return answer