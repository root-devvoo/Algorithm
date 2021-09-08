# 11022

test_case = int(input()) # 몇 번 출력할지 정함

for i in range(test_case):
    A, B = map(int, input().split())
    print('Case #%s: %s + %s = %s'%(i+1, A, B, A+B)) 
         
         # 변수를 문자열과 함께 출력할 때 연결(concatenating)을 사용한다.
         # %d(정수), %s(문자열), %f(실수)
