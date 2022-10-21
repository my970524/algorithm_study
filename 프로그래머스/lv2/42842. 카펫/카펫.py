def get_yellow_cases(num):
    m = int(num ** 0.5)
    result = []
    for i in range(1, m+1):
        if num % i == 0:
            result.append((i, num//i))
            if i != num // i:
                result.append((i, i))
    return result

def solution(brown, yellow):
    answer = []
    brown_without_corner = brown - 4
    yellow_cases = get_yellow_cases(yellow)

    for case in yellow_cases:
        if (case[0] + case[1]) * 2 == brown_without_corner:
            answer.append(case[0] + 2)
            answer.append(case[1] + 2)

    answer.sort(reverse=True)
    return answer