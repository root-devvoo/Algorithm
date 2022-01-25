T = int(input())

for _ in range(T):
    # bin 함수로 2진수 변환
    n = bin(int(input()))[2:] # 0b를 제외한 숫자만 사용하기 위해서 [2:] 사용
    # 최하위 비트(least significant bit, lsb)의 위치는 0
    for i, v in enumerate(n[::-1]): # 그러므로, 역순으로 탐색한다.
        if v == '1': # (bin 함수는 문자열로 반환한다, 그래서 따옴표로 감싸야 함)
            print(i, end=" ") # 1이 있는 인덱스 반환(출력)
