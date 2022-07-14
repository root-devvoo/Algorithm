def solution(s):
    answer = True
    stack = []

    # for문 반복문을 돌려서 괄호를 판별
    for s2 in s:
				# 열려있는 괄호면 무조건 스택에 추가
        if s2 == '(':
            stack.append(s2)
				# 닫혀있는 괄호면
        elif s2 == ')':
						# 스택에 뭐라도 있는 경우 (무조건 '(' 이 들어있는 경우)
            if stack:
                stack.pop()
						# 스택에 아무것도 없으면 ')' 을 스택에 추가
            else:
                stack.append(s2)
                break

		# 스택 안에 요소가 있냐 없냐로 결과값 판별
    if not stack: # 스택이 다 비어있으면,
        answer = True # 짝들이 다 맞아서 비어있는 것이므로 True
    else: # 스택이 비어있지 않다면
        answer = False # 짝들이 안맞아서 남아있는 것이므로 False

    return answer
