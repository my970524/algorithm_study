from collections import deque
import math

def get_rest_days(progress, speed):
    return math.ceil((100 - progress) / speed)

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    # 기능별로 남은 작업일수 구하기
    rest_days = deque()
    for i in range(n):
        progress = progresses[i]
        speed = speeds[i]
        rest_days.append(get_rest_days(progress, speed))
    print(rest_days)
    
    deploy = 0
    feat1 = rest_days[0]
    while rest_days:
        feat2 = rest_days.popleft()
        if feat1 >= feat2:
            deploy += 1
        else:
            answer.append(deploy)
            deploy = 1
        feat1 = max(feat1, feat2)
    answer.append(deploy)

    return answer


