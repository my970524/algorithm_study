def solution(phone_number):
    phone_list = list(phone_number)
    for i in range(len(phone_list)-4):
        phone_list[i] = '*'
    return ('').join(phone_list)
    