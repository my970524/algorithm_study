def solution(arr):
    if len(arr) == 1:
        return [-1]
    min = sorted(arr)[0]
    arr.remove(min)
    return arr
