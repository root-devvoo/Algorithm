# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution(money):
	coin = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
	counter = 0 # 최소 동전의 개수
	idx = len(coin) - 1
	while money:
		counter += (money // coin[idx]) # 빈칸
		money %= coin[idx] # 빈칸
		idx -= 1 # 빈칸
	return counter

##########################################################
money = 2760
ret = solution(money)

print("solution 함수의 반환 값은", ret, "입니다.")