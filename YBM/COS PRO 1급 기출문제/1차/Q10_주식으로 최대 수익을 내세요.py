# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(prices):
	INF = 1000000001; # 큰 수
	tmp = INF # 큰 수 초기값 :: 작은 수를 찾을 때 이런식으로 많이 함 :: 가장 적은 구매 가격
	answer = -INF # 작은 수 초기값 :: 큰 수를 찾을 때 :: 최대 수익
	for price in prices: # price :: 현 가격
		if tmp != INF: # 구매한 적이 있다면,
			answer = max(answer, price - tmp) # 한 줄 수정한 부분, (판매가격 - 구매가격 이 되어야함)
		tmp = min(tmp, price) # 가장 쌀 때 구매한 가격
	return answer # 최대 수익
#####################################################################################
prices1 = [1, 2, 3];
ret1 = solution(prices1);

print("solution 함수의 반환 값은", ret1, "입니다.")
    
prices2 = [3, 1];
ret2 = solution(prices2);

print("solution 함수의 반환 값은", ret2, "입니다.")