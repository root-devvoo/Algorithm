N, M = map(int, input().split())
# 듣도 못한 사람
dutdo = set()
for _ in range(N):
    dutdo.add(input())

# 보도 못한 사람
bodo = set()
for _ in range(M):
    bodo.add(input())

# 듣보잡 결과 리스트 만들기
result = sorted(list(dutdo & bodo))
# 듣보잡 결과 출력
print(len(result))
for db in result:
    print(db)
