def count_alph_change(alph):
    alph_dic = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':12, 'P':11, 'Q':10, 'R':9, 'S':8, 'T':7, 'U':6, 'V':5, 'W':4, 'X':3, 'Y':2, 'Z':1}

    return alph_dic[alph]

def solution(name):
    answer = 0
    n = len(name)
    move = n - 1

    # 알파벳 바꾸면서 생기는 조이스틱의 상하 움직임 횟수를 answer에 먼저 더해준다.    
    for alph in name:
        answer += count_alph_change(alph)
    
    for i in range(n):
        # next_i란 단순히 다음 인덱스가 아닌, 알파벳 변경이 필요한 다음 인덱스를 뜻함
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            # 그렇기 때문에 next_i가 맨 마지막 인덱스가 아니고,
            # next_i의 자리가 A라면, A를 계속 건너뛰기 위해 아래와 같이 진행
            next_i += 1
        
        # 정방향으로 가기, 정방향으로 가다가 역방향으로 가기, 역방향으로 가다가 정방향으로 돌아오기
        # 세 가지 경우를 비교
        move = min(move, i + i + (n-next_i), i + (n-next_i) * 2)

    answer += move
    return answer