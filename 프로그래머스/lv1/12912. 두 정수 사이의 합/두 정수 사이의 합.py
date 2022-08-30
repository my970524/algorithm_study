def solution(a, b):
    nums = []
    if a < b:
        for i in range(a, b+1):
            nums.append(i)
    else:
        for i in range(b, a+1):
            nums.append(i)
    answer = sum(nums)           
    return answer