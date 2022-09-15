from collections import deque

def solution(queue1, queue2):
    answer = 0
    limit = len(queue1) * 3
    # deque 사용
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    # 반복할때마다 sum 하지 않기 위해 각 큐의 합을 변수로 지정하고 값을 더하고 뺀다.
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)

    # 두 큐의 합이 홀수라면 -1 return
    if (sum_queue1 + sum_queue2) % 2 != 0:
        return -1
    
    # 두 큐의 합이 같아질때 까지
    # 각 큐의 합을 비교해서 합이 큰 큐에서 작은 큐로 원소를 준다.
    for i in range(limit):
        # 두 큐의 합이 같아지면 return answer
        if sum_queue1 == sum_queue2:
            return answer
        if sum_queue1 > sum_queue2:
            num = queue1.popleft()
            queue2.append(num)
            sum_queue2 += num
            sum_queue1 -= num
            answer += 1
        else:
            num = queue2.popleft()
            queue1.append(num)
            sum_queue1 += num
            sum_queue2 -= num
            answer += 1
    # limit 까지 돌아도 두 큐의 합이 같아지지 않으면 return -1
    return -1