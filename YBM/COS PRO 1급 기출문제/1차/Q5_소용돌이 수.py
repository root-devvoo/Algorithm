## 2번
# n = 4
# dir = 0 # 0 1 2 3 0 1 2 3 0 1 2 3 ...
# loop = n
# r, c = 0, -1
# dr = [0, 1, 0, -1] # 각각 dir이 0일때, 1일때, 2일때, 3일때의 r(행)의 변량
# dc = [1, 0, -1, 0] # column의 변량: 처음에 1(column 증가) 0(column 변화없음), -1(column 감소), 0(column 변화없음)
# for _ in range(n*2-1):
#     for _ in range(loop):
#         r += dr[dir]
#         c += dc[dir]
#         print(f'[{r}, {c}]', end=' ')
#     # print(f'[{dir}, {loop}]', end=' ')
#     dir = (dir + 1) % 4
#     if dir % 2 : loop -= 1 # dir을 2로 나눈 나머지가 홀수라면, loop에 대해서 1 감소

## 이해를 위한 부분
# n = 5
# 9회
# 0 1 2 3 0 1 2 3 0
# 5 4 4 3 3 2 2 1 1

# n = 4
# 7회
# 0 1 2 3 0 1 2 (dir)
# 4 3 3 2 2 1 1 (loop)

# n = 3
# 5회
# 0 1 2 3 0
# 3 2 2 1 1

## 1번째
# n = 4
# dir = 0 # 0 1 2 3 0 1 2 3 0 1 2 3 ...
# loop = n
# for _ in range(n*2-1):
#     print(f'[{dir}, {loop}]', end=' ')
#     dir = (dir + 1) % 4
#     if dir % 2 : loop -= 1 # dir을 2로 나눈 나머지가 홀수라면, loop에 대해서 1 감소

#####################################################################################################
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(n):
	a = [ [0] * n for _ in range(n) ] # n x n만큼 0으로 채운 테이블 생성
	dir = 0 # 방향 0 1 2 3 0 1 2 3 0 1 2 3 ...
	loop = n # 해당 방향으로 채우는 숫자 개수
	r, c = 0, -1 # 좌표의 초기값
	dr = [0, 1, 0, -1] # 방향에 대한 r의 변량
	dc = [1, 0, -1, 0] # 방향에 대한 c의 변량
	num = 0
	while num < n*n:
		for _ in range(loop):
			r += dr[dir]
			c += dc[dir]
			num += 1
			a[r][c] = num
			# print(f'[{r}, {c}] = {num}', end=' ')
				
		dir = (dir + 1) % 4
		if dir % 2 : loop -= 1 # dir을 2로 나눈 나머지가 홀수라면, loop에 대해서 1 감소
	# print(a)
	answer = 0
	for i in range(n):
		answer += a[i][i] # a의 [0][0], a[1][1], a[2][2], a[3][3]
	return answer
###########################################################################################
n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
    
n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")    