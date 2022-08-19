def solution(array, commands):
    answer = []
    
    for command in commands:
        start = command[0] - 1
        end = command[1]
        arr = array[start:end]
        arr.sort()
        answer.append(arr[command[2]-1])    
    return answer