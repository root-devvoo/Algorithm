# 문자열 p를 두 "균형잡힌 괄호 문자열" u, v로 분리하는 함수
def divide(p):
    open_bracket = 0
    close_bracket = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            open_bracket += 1
        else:
            close_bracket += 1
        # 열려있는 괄호의 수와 닫혀있는 괄호의 수가 같다면 (짝이 맞는거니까)
        if open_bracket == close_bracket:
            # 같은 순간에 0번 인덱스부터 i+1번째 인덱스까지, i+1번째부터 끝까지 (슬라이싱을 이용해서) 나눠 리턴
            return p[:i+1], p[i+1:]

# u가 "올바른 괄호 문자열" 인지 판별 하는 함수
def checkBracket(u):
    stack = []
    
    for s in u:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                stack.pop()
            else:
                stack.append(s)
                break
    if not stack:
        return True
    else:
        return False

# main   
def solution(p):
    answer = ''
    
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not p: return ''
    # 2. 문자열을 두 "균형잡힌 괄호 문자열" u, v로 분리
    u, v = divide(p)
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    if checkBracket(u):
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        return u + solution(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        answer = '('
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        answer += solution(v)
        # 4-3. ')'를 다시 붙입니다.
        answer += ')'
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        for u2 in u[1 : len(u)-1]:
            if u2 == '(':
                answer += ')'
            else:
                answer += '('
                
        # 4-5. 생성된 문자열을 반환        
        return answer  
