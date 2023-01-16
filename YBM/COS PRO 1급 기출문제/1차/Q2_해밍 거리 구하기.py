def func_a(string, length):
	padZero = ""
	padSize = length - len(string) # 빈칸
	# max_length - 문자열 길이 => padSize
	# padSize란 다른 2진수 문자열의 크기보다 모자른 양
	for i in range(padSize):
		padZero += "0"
	return padZero + string

def solution(binaryA, binaryB):
	max_length = max(len(binaryA), len(binaryB))
	binaryA = func_a(binaryA, max_length)
	binaryB = func_a(binaryB, max_length)

	hamming_distance = 0
	for i in range(max_length):
		if binaryA[i] != binaryB[i]: # 빈칸
			hamming_distance += 1
	return hamming_distance
########################################################
binaryA = "10010"
binaryB = "110"
ret = solution(binaryA, binaryB)

print("solution 함수의 반환 값은", ret, "입니다.")