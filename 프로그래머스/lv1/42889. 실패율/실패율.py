def solution(N, stages):
    challengers = len(stages)
    fail_por = {}
    # for i in range(1, N+1):
    #     if len(list(filter(lambda n : n >= i, stages))) == 0:
    #         fail_por[i] = 0
    #     else:
    #         fail_por[i] = stages.count(i) / len(list(filter(lambda n : n >= i, stages)))
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