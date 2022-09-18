def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = 0
    # 체육복을 잃어버리지 않아서 수업을 들을 수 있는 학생 수 먼저 세기
    answer += n - len(lost)
    # 여벌이 있지만 잃어버렸다면
    lost_and_reserve = list(set(lost) & set(reserve))
    if lost_and_reserve:
        for i in lost_and_reserve:
            answer += 1
            lost.remove(i)
            reserve.remove(i)

    # 체육복을 빌릴 수 있는지 확인하고, 빌릴 수 있으면 answer에 추가
    while lost:
        l = lost.pop()
        # l보다 큰 학생에게서 빌릴 수 있다면
        if l+1 in reserve:
            answer += 1
            reserve.remove(l+1)
        # l보다 작은 학생에게서 빌릴 수 있다면
        elif l-1 in reserve:
            answer += 1
            reserve.remove(l-1)
    return answer