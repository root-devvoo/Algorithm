test_case = int(input()) # 몇 번 출력할지 정함

for i in range(test_case): # i 라는 변수를 사용하지 않겠다라는 의미로 _(언더바)를 사용해도 좋다
    A, B = map(int, input().split())
    print('Case #%s: %s'%(i+1, A+B)) 
         # 변수를 문자열과 함께 출력할 때 연결(concatenating)을 사용한다.
         # %d(정수), %s(문자열), %f(실수) 
