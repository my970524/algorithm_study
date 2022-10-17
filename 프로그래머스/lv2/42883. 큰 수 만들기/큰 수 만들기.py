def solution(number, k):
    answer = []
    answer_len = len(number) - k
    for i in number:
        # answer가 비어있지 않고
        # answer의 마지막 요소가 i보다 작고
        # k가 0 보다 크다면 
        # 계속해서 answer의 값을 제거하면서 k 횟수 차감
        while answer and answer[-1] < i and k > 0:
            answer.pop()
            k -= 1
        # while문 탈출 후 answer에 현재 i 추가
        answer.append(i)
    # number=1000000, k=3 과 같은 경우에는 answer에 i를 추가만 하기 때문에
    # 마지막에 answer_len 만큼 길이를 자르는 과정 필요
    answer = answer[:answer_len]
    return ''.join(answer)


                
            
    
    
            