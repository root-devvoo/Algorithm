# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(num):
	answer = int(str(num+1).replace('0', '1')) # 빈칸
	return answer
####################################################
num = 9949999;
ret = solution(num)

print("solution 함수의 반환 값은", ret, "입니다.")