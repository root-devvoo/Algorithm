while True:
    str = input()
    stack = []
    
    # 마침표가 나오면 break 걸어줌 
    # (stack이 비어있는 상태에서 마침표로만 끝나도 yes로 간주)   
    if str == '.':
        break 
    
    # 괄호 판별
    for c in str:
        if c == '[' or c == '(':
            stack.append(c)    
        elif c == ']':
            # 스택에 비어있지 않으면서 짝이 맞는 '[' 괄호가 있다면
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            # 스택에 조건에 맞는 괄호가 없는 경우
            else:
                stack.append(']')
                break
        elif c == ')':
            # 스택에 비어있지 않으면서 짝이 맞는 '(' 괄호가 있다면
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            # 스택에 조건에 맞는 괄호가 없는 경우  
            else:
                stack.append(')')
                break       
    # 최종 결과 판별
    if len(stack) == 0:
        print('yes')
    else:
