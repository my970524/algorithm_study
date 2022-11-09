from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    passing = deque([0] * bridge_length)
    passed = 0
    cur_weight = 0
    n = len(truck_weights)

    while passed < n:
        answer += 1
        out = passing.popleft()
        if out != 0:
            passed += 1
        cur_weight -= out
        if truck_weights:
            new = truck_weights[0]
            if cur_weight + new <= weight:
                passing.append(truck_weights.popleft())
                cur_weight += new
            else:
                passing.append(0)
    return answer