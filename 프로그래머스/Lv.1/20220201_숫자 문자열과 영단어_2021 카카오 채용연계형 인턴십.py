# 프로그래머스 lv.1 숫자 문자열과 영단어
def solution(s):
    answer = s # s를 그대로 받아서 정답 변수에 넣음
    dic_words = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
                'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    for k, v in dic_words.items(): # items함수는 딕셔너리의 key, value를 반환
        answer = answer.replace(k, v) # replace는 문자열을 변경하는 함수,
                                      # 문자열 안에서 특정 문자를 새로운 문자로 변경
                                      # 여기서는, 문자로 되있는 것을 숫자로 바꾸도록 함
    return int(answer)
