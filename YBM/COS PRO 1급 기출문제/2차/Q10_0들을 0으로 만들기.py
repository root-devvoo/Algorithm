# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(s): # "101100011100"
	s += '#'
	answer = ""
	for i in range(len(s)):
		if s[i] == '0' and s[i + 1] != '0': # 1011
			answer += '0'
		elif s[i] == '1': # 한 줄 바꾼 부분
			answer += '1'
	return answer

#####################################################
s = "101100011100"
ret = solution(s)

print("solution 함수의 반환 값은", ret, "입니다.")