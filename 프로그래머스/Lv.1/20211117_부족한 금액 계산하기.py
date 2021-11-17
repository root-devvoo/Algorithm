def solution(price, money, count):
    
    result = 0
    
    for N in range(1, count+1):
        result += price*N
        # 처음 이용료가 100이면 2번째에는 200, 3번째에는 300
        # 이런식으로 놀이기구를 N번째 이용한다면 원래 이용료의 N배를 받는다        
        
    if result >= money: # 내가 가지고 있는 돈이 모자를 경우
        answer = result-money
        # 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지 return
    
    else:
        answer = 0
        # 금액이 부족하지 않으면 0을 return
        
    return answer
