def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    left_only = [1, 4, 7]
    right_only = [3, 6, 9]

    for number in numbers:
        if number in left_only:
            answer += 'L'
            left = number
        elif number in right_only:
            answer += 'R'
            right = number
        else:
            if number == 0:
                number = 11

            left_dis = abs(left-number) // 3 + abs(left-number) % 3
            right_dis = abs(right-number) // 3 + abs(right-number) % 3
            if left_dis < right_dis:
                answer += 'L'
                left = number
            elif left_dis > right_dis:
                answer += 'R'
                right = number
            else:
                if hand == 'left':
                    answer += 'L'
                    left = number
                else:
                    answer += 'R'
                    right = number
    return answer
