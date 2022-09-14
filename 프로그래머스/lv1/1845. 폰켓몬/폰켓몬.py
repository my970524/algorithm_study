def solution(nums):
    set_nums = list(set(nums))
    
    if len(nums)/2 <= len(set_nums):
        return len(nums)/2
    return len(set_nums)