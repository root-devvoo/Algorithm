# 50점짜리 답안
L = int(input())
alphabets = input()
result = 0

for i in range(L):
    # ord함수로 아스키코드 값을 반환
    # a~z는 97~122 이므로 96을 빼주면 원하는 숫자로 매칭됨
    result += (ord(alphabets[i]) - 96) * (31 ** i) # 힌트 예제 1 참고

print(result)
############################ 정답(100점) ############################
L = int(input())
alphabets = input()
result = 0

for i in range(L):
    # ord함수로 아스키코드 값을 반환
    # a~z는 97~122 이므로 96 빼주면 원하는 숫자로 매칭됨
    result += (ord(alphabets[i]) - 96) * (31 ** i) # 힌트 예제 1 참고

print(result % 1234567891)
# mod는 나머지 연산을 의미함.
# 결과값과 숫자 M인 1234567891과 나머지 연산을 해주면 됨. 
