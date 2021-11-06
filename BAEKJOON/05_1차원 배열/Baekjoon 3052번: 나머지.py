result = []

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다
for _ in range(10):
    number = int(input())
    result.append(number % 42) # 나머지를 구해서 result 리스트에 넣어준다

result = set(result) # 서로 다른 나머지가 몇개 있는지 출력하기 위해 중복되는 값을 set으로 형 변환하여 없애주고 덮는다
print(len(result))
