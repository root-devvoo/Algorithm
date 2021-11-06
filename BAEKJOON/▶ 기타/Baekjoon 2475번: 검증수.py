id_num = list(map(int, input().split()))
ver_num = []

for i in range(len(id_num)):
   ver_num.append(id_num[i] ** 2) 
   
print(sum(ver_num) % 10)
# 검증수 :: 고유번호의 각 숫자를 제곱한 수들의 합을 10으로 나눈 나머지
