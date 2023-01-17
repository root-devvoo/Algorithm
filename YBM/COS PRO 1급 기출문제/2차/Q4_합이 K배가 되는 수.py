# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from itertools import combinations # 조합: 서로 다른 n개 중에 r개를 선택하는 경우의 수(순서 X) 구함

def solution(arr, K):
	answer = 0
	for c in combinations(arr, 3):
		if (sum(c) % K) == 0:
			answer += 1
	return answer
############################################################################################
arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")