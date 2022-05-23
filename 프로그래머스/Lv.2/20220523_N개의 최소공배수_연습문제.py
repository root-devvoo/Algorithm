from math import gcd
# gcd == 최대공약수

def solution(arr):
    # 최소공배수 구하는 함수
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]
    '''
    먼저, 2개의 수에 대해 최소공배수를 구한다.
    그 다음, 그 값과 계산하지 않은 값들 중 1개를 선택해 다시 최소공배수를 구한다.
    '''
