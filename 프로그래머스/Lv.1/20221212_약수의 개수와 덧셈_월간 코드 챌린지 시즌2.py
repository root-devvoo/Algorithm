# 약수의 개수를 return 해주는 함수
def get_divisor(n):
    index = 1
    count = 0
    
    while index <= n:
        if n % index == 0: # 나머지가 0이면 약수니까,
            count += 1 # 개수를 추가
        index += 1 # 나머지가 0이 아닐 경우 1을 index에 더해줘서 while문이 순차적으로 돌게 만듬
        
    return count

#  left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 해주는 함수
def solution(left, right):
    answer = 0
    
    for n in range(left, right+1):
        if get_divisor(n) % 2 == 0:
            answer += n # 약수의 개수가 짝수인 경우 더함
        else:
            answer -= n # 약수의 개수가 홀수인 수는 빼줌
        
    return answer
