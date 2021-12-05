n, k = map(int, input().split())

count = 0

coin_type = []
# n개의 줄에 동전의 가치가 오름차순으로 주어진 것을 리스트에 넣는다
for _ in range(n):
    coin_type.append(int(input()))

coin_type.sort(reverse=True)
# 동전 개수의 최솟값을 출력하려면 동전의 가치가 큰 순서대로 계산해야하므로 내림차순으로 정렬    

# k원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
for coin in coin_type:
    count += k // coin
    k %= coin

print(count)
