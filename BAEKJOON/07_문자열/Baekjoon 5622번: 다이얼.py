alphabets = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
dial = input()

second = 0

for i in range(len(dial)):
    for a in alphabets: 
        if dial[i] in a: # 만약 dial i번째 글자가 alphabets의 요소 중에 있는 경우
            second += alphabets.index(a)+3 # dial 입력한 것과 똑같은 알파벳이 있는 인덱스를 구한 다음에 3을 더해 초 변수에 담아준다
            # (글자가 있는 다이얼을 입력할 때는 최소 숫자 2에서부터 입력.. 그렇기 때문에 3초부터 시간이 걸리므로 3을 더함)

print(second)
