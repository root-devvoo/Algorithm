test_case = int(input())

for _ in range(test_case): # i 라는 변수를 사용하지 않겠다라는 의미로 _(언더바)를 사용해도 좋다
    input_data = input().split(' ')
    A = int(input_data[0])
    B = int(input_data[1])
    print(A + B)
