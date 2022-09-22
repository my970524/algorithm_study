def solution(s):
    answer = True
    stack = []
    if s[0] == ')':
        return False
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                stack.pop()
    return stack == []