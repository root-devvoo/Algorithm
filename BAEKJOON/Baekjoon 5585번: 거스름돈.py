price = 1000 - int(input())
# 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구해야하니까 1000을 빼줌
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    count += price // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    price %= coin

print(count)
