# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# record를 이길 수 있는 방법을 반환
def func(record):
	if record == 0: # 가위 - 바위 반환
		return 1
	elif record == 1: # 바위 - 보 반환
		return 2
	return 0 # 보 - 가위 반환

def solution(recordA, recordB):
	cnt = 0 # A의 계단 위치
	# a = []
	for i in range(len(recordA)):
		if recordA[i] == recordB[i]: # 비긴 경우
			# a.append(cnt)
			continue
		elif recordA[i] == func(recordB[i]): # 이긴 경우
			cnt = cnt + 3
		else: # 진 경우
			cnt = max(0, cnt-1) # 한 줄 수정한 부분: 0과 cnt-1을 비교해서 더 큰 값을 갖도록
		# a.append(cnt)
	
	# print(a)
	return cnt
######################################################################################
recordA = [2,0,0,0,0,0,1,1,0,0]
recordB = [0,0,0,0,2,2,0,2,2,2]
ret = solution(recordA, recordB)


print("solution 함수의 반환 값은", ret, "입니다.")