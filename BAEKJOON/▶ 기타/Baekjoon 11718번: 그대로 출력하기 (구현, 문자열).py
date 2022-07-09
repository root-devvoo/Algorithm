while True:
    try:
        print(input())
    except EOFError: # 예외 처리문
        break
