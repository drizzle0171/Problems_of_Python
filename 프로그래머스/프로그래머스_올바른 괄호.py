def solution(s):
    if s[0] == ')':
        answer = False
    else:
        if s.count('(') == s.count(')'):
            answer = True
        else:
            answer = False
    return answer

print(solution('(()('))

# stack....que....

def solution(s):
    stack = []
    for i in s:
        if i == '(':  # '('는 stack에 추가
            stack.append(i)
        else:  # i == ')'인 경우
            if stack == []:  # 괄호 짝이 ')'로 시작하면 False 반환
                return False
            else:
                stack.pop()  # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거
    
    return stack==[]

    ### 다시 공부 !!!