# # 1. "A7" -> 좌표
# # A7같은 경우는 (0, 6)으로 바꿈
# # 아스키 값 :: ord('A'): 65, ord('a'): 97, ord('0'): 48
# pos = "A7"
# c = ord('A') - ord('A') # 0
# r = ord('7') - ord('1') # 6
# # "A7"의 새로운 좌표값은 [0 6]이 되도록 바꿨다.

# # 2. 8방향 돌며 좌표, 체스판 내부/외부 내부인 것만 count세는 것
# dr = [2, 1, -1, -2, -2, -1, 1, 2]
# dc = [1, 2, 2, 1, -1, -2, -2, -1]
# # A7 좌표
# r, c = 6, 0
# answer = 0
# for i in range(8):
#     nr = r + dr[i]
#     nc = c + dc[i]
#     # 이동할 수 있는 범위 안의 좌표에 대해서만 결과가 나오도록
#     if nr>=0 and nr<8 and nc>=0 and nc<8: 
#         answer += 1
#         #print(nr, nc)

# print(answer)

def solution(pos):
    c = ord(pos[0]) - ord('A')
    r = ord(pos[1]) - ord('1')
    dr = [2, 1, -1, -2, -2, -1, 1, 2]
    dc = [1, 2, 2, 1, -1, -2, -2, -1]
    answer = 0
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        # 이동할 수 있는 범위 안의 좌표에 대해서만 결과가 나오도록
        if nr>=0 and nr<8 and nc>=0 and nc<8: 
            answer += 1
    return answer
##############################################################
pos = "A7"
ret = solution(pos)

print("solution 함수의 반환 값은", ret, "입니다.")    