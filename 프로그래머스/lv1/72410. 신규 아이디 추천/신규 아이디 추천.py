def solution(new_id):
    answer = []
    not_allow = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', ']', '{', '}', ':', '?', ',', '<', '>', '/']
    # 1단계 모두 소문자로
    new_id = new_id.lower()
    print(f'1단계 실행: {new_id}')
    # 2단계 불필요한 문자열 제거
    for i in new_id:
        if i in not_allow:
            new_id = new_id.replace(i, '')
    print(f'2단계 실행: {new_id}')
    # 3단계 연속된 . 을 하나의 .으로 치환
    for i in range(len(new_id)-1):
        if new_id[i] == '.' and new_id[i] == new_id[i+1]:
            pass
        else:
            answer.append(new_id[i])
    answer.append(new_id[-1])
    print(f'3단계 실행: {("").join(answer)}')
    # 4단계 .이 맨 앞이나 맨 뒤에 있으면 제거
    if answer and answer[0] == '.':
        answer.pop(0)
    if answer and answer[-1] == '.':
        answer.pop()
    print(f'4단계 실행: {("").join(answer)}')
    # 5단계 빈 문자열이라면 'a'대입
    if not answer:
        answer.append('a')
    print(f'5단계 실행: {("").join(answer)}')
    # 6단계 길이가 16이상이면 15개까지만 남기고, 맨 끝에 .이 있으면 제거
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer.pop()
    print(f'6단계 실행: {("").join(answer)}')
    # 7단계 길이가 2 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 붙이기
    if len(answer) <= 2:
        while len(answer) != 3:
            answer.append(answer[-1])
    print(f'7단계 실행: {("").join(answer)}')
    return ('').join(answer)