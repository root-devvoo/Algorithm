from itertools import permutations
# permutations() 함수는 순열을 만드는 함수
# 순열 :: 서로 다른 n개의 원소에서 r개를 중복없이 순서에 상관있게 선택하는 혹은 나열하는 것

# 소수 구하는 함수 정의 (에라토스테네스의 체 아님)
def isPrime(n):
    if(n<2):
        return False
    
    for i in range(2, n):
        if(n%i == 0):
            return False
    
    return True
            
def solution(numbers):
    answer = []
    numbers = list(numbers)
    tmp = []
    
    for i in range(1, len(numbers)+1):
        tmp += list(permutations(numbers, i)) # numbers에서 i개씩 순열 조합
    # 각 순열 조합을 정수로 변환
    number = [int(''.join(s)) for s in tmp]
    # ''.join(리스트)를 이용하면 매개변수로 들어온 ['1', '7'] 이런 식의 리스트를 
    # '17'과 같은 문자열로 합쳐서 반환 (참고 : https://blockdmask.tistory.com/468)
    
    for n in number: # 순열 조합을 넣은 number의 요소 중에서
        if isPrime(n): # 소수 판별... 소수면,
            answer.append(n) #  answer 리스트에다가 append
    
    return len(set(answer)) # set으로 형 변환해서 중복 제거 후 소수의 개수 반환
