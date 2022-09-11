def solution(id_list, report, k):
    # 중복 신고 제거
    report = set(report)
    # 신고받은 사람의 횟수를 기록할 딕셔너리 get_reported 생성
    # id_list에 담긴 유저별로 신고받은 횟수를 0으로 초기화
    get_reported = {id:0 for id in id_list}
    # 각 유저별로 메일을 몇 개 받을지 기록할 딕셔너리 get_mail 생성
    # id_list에 담긴 유저별로 메일 받을 횟수를 0으로 초기화
    get_mail = {id:0 for id in id_list}
    
    # ' '를 기준으로 r을 쪼갰을 때, 1번 인덱스의 값이 신고받은 사람
    for r in report:
        get_reported[r.split(' ')[1]] += 1
    
    # report의 요소를 돌면서 신고받은 사람이 k번 이상 신고받았으면, 
    # 그 사람을 신고한 사람은 메일을 한 통 받는다.
    for r in report:
        if get_reported[r.split(' ')[1]] >= k:
            get_mail[r.split(' ')[0]] += 1
    
    # get_mail에서 value값만 list로 return 한다.
    return list(get_mail.values())