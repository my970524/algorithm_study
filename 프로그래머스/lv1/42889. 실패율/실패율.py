def solution(N, stages):
    challengers = len(stages)
    fail_por = {}
    # 1번 스테이지부터 실패율을 fail_por에 기록   
    for i in range(1, N+1):
        failures = stages.count(i)
        if challengers == 0:
            fail_por[i] = 0
        else:
            fail_por[i] = failures / challengers
            challengers -= failures
    fail_por = dict(sorted(fail_por.items(), key=lambda item: item[1], reverse=True))
    answer = list(fail_por.keys())
    return answer