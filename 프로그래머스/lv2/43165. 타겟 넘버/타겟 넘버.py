def solution(numbers, target):
    answer = 0
    stack = [[numbers[0], 0], [-1*numbers[0], 0]]
    n = len(numbers)
    
    # stack이 비어질 때까지 반복
    while stack:
        # 값(v)와 인덱스(i) 추출
        v, i = stack.pop() 
        # 다음 인덱스 값 비교를 위해 i를 하나 증가
        i += 1
        
        # i가 n보다 작다는건 numbers의 모든 인덱스를 돌지 않았다는 뜻
        if i < n:
            # 현재 값(v)와 numbers의 다음 인덱스 값을 더한 값과 다음 인덱스를 스택에 넣어준다.
            # 현재 값(v)와 numbers의 다음 인덱스 값을 빼준 값(다음 인덱스 값에 - 부호를 붙인               설정)과 다음 인덱스를 스택에 넣어준다.
            stack.append([v+numbers[i], i])
            stack.append([v-numbers[i], i])
        # i가 n보다 작지 않다는건 numbers의 모든 인덱스를 돌았다는 뜻
        else:
            # 마지막 인덱스까지 돌고난 뒤의 v가 target과 같다면
            if v == target:
                answer += 1
    return answer