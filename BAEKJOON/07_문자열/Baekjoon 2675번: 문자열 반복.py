n = int(input())

for _ in range(n):
    R, S = input().split()
    for i in S:
        print(i * int(R), end='') 
    print() # 개행하지 않고 한줄로 출력되도록 end='' 사용하고, 
    # 다음줄로 넘어가도록 print() 추가
