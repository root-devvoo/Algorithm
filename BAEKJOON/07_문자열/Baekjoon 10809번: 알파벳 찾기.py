import sys
input = sys.stdin.readline()

S = input
alphabet = list(range(97, 123)) # 소문자들 아스키코드 range

for i in alphabet:
    print(S.find(chr(i))) # chr() 아스키코드 → 문자
    # find() 는 찾는 문자가 문자열 안에 포함되지 않은 경우 -1을 출력
