# 집합 A의 원소의 개수(AL), 집합 B의 원소의 개수(BL)
AL, BL = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A-B) + len(B-A))
