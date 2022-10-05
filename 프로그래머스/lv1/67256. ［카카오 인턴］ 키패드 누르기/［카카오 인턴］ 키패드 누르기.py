# def solution(numbers, hand):
#     # numbers의 0을 11로 바꿔주기
#     if 0 in numbers:
#         zero_index = numbers.index(0)
#         numbers[zero_index] = 11

#     answer = ''
#     left = 10
#     right = 12
#     left_only = [1, 4, 7]
#     right_only = [3, 6, 9]

#     for number in numbers:
#         if number in left_only:
#             answer += 'L'
#             left = number
#         elif number in right_only:
#             answer += 'R'
#             right = number
#         else:
#             left_dis = abs(left-number) // 3 + abs(left-number) % 3
#             right_dis = abs(right-number) // 3 + abs(right-number) % 3
#             if left_dis < right_dis:
#                 answer += 'L'
#                 left = number
#             elif left_dis > right_dis:
#                 answer += 'R'
#                 right = number
#             else:
#                 if hand == 'left':
#                     answer += 'L'
#                     left = number
#                 else:
#                     answer += 'R'
#                     right = number
#     return answer
def solution(numbers, hand):
    answer = ''
    L_cur = 10
    R_cur = 12
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += "L"
            L_cur = n
        elif n == 3 or n == 6 or n == 9:
            answer += "R"
            R_cur = n
        else:
            if n == 0:
                n = 11
                
            L_dis = abs(L_cur-n) // 3 + abs(L_cur-n) % 3
            R_dis = abs(R_cur-n) // 3 + abs(R_cur-n) % 3
            
            if L_dis > R_dis:
                answer += "R"
                R_cur = n
            elif R_dis > L_dis:
                answer += "L"
                L_cur = n
            else:
                if hand == "right":
                    answer += "R"
                    R_cur = n
                else:
                    answer += "L"
                    L_cur = n
    return answer