def to_bin(num, n):
    bin_num = bin(num)[2:]
    if len(bin_num) < n:
        bin_num = '0' * (n - len(bin_num)) + bin_num
    return list(bin_num)

def solution(n, arr1, arr2):
    answer = []
    code = ''
    map1 = []
    map2 = []
    for i in arr1:
        map1.append(to_bin(i, n))
    for i in arr2:
        map2.append(to_bin(i, n))
    
    for i in range(n):
        for j in range(n):
            if map1[i][j] == '0' and map2[i][j] == '0':
                code += ' '
            else:
                code += '#'
        answer.append(code)
        code = ''
    
    return answer