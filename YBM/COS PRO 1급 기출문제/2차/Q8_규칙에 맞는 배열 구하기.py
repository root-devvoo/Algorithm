# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(arr):
	left, right = 0, len(arr) - 1
	idx = 0 # 새로운 리스트에 숫자를 넣을 위치
	answer = [0 for _ in range(len(arr))] # 새로운 리스트
	while left <= right: # 0 <= 5  1 <= 5  1 <= 4
		if idx % 2 == 0: # 0 % 2  1 % 2  1 % 2, !!! 여기 부분 이상하므로 고쳐야 할 부분
			answer[idx] = arr[left] # answer = [1, 0, 0, 0, 0, 0]
			left += 1 # left = 1
		else:
			answer[idx] = arr[right]
			right -= 1 # right = 4
		idx += 1 # idx = 2
	return answer
# 한 줄 채우기 문제는 이런식으로(주석과 같이) 하나씩 종이에 적으면서 흐름을 파악해서 이상한 부분을 찾아내자.
################################################################################
arr = [1, 2, 3, 4, 5, 6]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")