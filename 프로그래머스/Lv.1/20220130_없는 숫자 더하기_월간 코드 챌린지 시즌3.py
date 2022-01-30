# 프로그래머스 lv.1 없는 숫자 더하기
def solution(numbers):
    answer = 0
    for n in range(10):
        if n not in numbers:
            answer += n
    return answer
