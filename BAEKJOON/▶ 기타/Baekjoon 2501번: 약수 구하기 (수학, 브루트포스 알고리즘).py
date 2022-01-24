N, K = map(int, input().split())
divisor_list = []

for i in range(1, N+1):
    if N % i == 0:
        # 약수
        divisor_list.append(i)
        
# 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력
if len(divisor_list) < K:
    print(0)
# 그렇지 않으면, N의 약수들 중 K번째로 작은 수를 출력한다.
else:
    print(divisor_list[K-1])
