input_data = list(map(int, input().split(' ')))

# 1 2 3
# ['1', '2', '3']
# => [1, 2, 3]
input_data.sort() # 정렬하고
print(input_data[1]) # 두번째로 큰 정수 출력
