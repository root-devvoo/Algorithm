while True:
    N = input()
    
    if N == '0':
        break
    
    if N == N[::-1]: # [::-1] 을 통해 문자열을 뒤집은 결과랑 같으면
        print('yes')
        
    else:
        print('no')
