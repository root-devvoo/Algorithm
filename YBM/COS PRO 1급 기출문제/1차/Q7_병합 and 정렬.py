def solution(arrA, arrB):
	arrA_idx = 0 # 리스트 A에서 현 위치
	arrB_idx = 0 # 리스트 B에서 현 위치
	arrA_len = len(arrA) # arrA 리스트의 요소 개수(길이 정보)
	arrB_len = len(arrB) # arrB 리스트의 요소 개수(길이 정보)
	answer = []
	while arrA_idx < arrA_len and arrB_idx < arrB_len: # 빈칸
	# 비교할 대상이 있는 경우에만 while문 돌도록, (양쪽에 비교 대상이 있는 경우 반복)
		if arrA[arrA_idx] < arrB[arrB_idx]:
			answer.append(arrA[arrA_idx])
			arrA_idx += 1
		else:
			answer.append(arrB[arrB_idx])
			arrB_idx += 1
	while arrA_idx < arrA_len: # 빈칸
	# arrA에 남은 item이 있는 경우 반복	
		answer.append(arrA[arrA_idx])
		arrA_idx += 1
	while arrB_idx < arrB_len: # 빈칸
	# arrB에 남은 item이 있는 경우 반복	
		answer.append(arrB[arrB_idx])
		arrB_idx += 1
	return answer
##############################################################################
arrA = [-2, 3, 5, 9]
arrB = [0, 1, 5]
ret = solution(arrA, arrB);

print("solution 함수의 반환 값은", ret, "입니다.")