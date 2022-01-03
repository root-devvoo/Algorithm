from collections import deque
# deque을 활용한 풀이

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        time = 0 # 시간(초) 세는 변수
        current = prices.popleft() # 떨어지기까지의 시간(초)을 구할 현재가
        
        for price in prices:
            time += 1 # for문이 한 바퀴 돌때마다 시간(초) 1씩 증가시키고,
            if price < current: # 만약 x초 뒤의 가격이 현재가보다 적은 경우
                break # for문을 빠져나오도록!
                
        answer.append(time) # 시간(초) 센 값을 answer(정답) 리스트에 넣어줌   
    return answer
