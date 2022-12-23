def solution(array):
    answer = ''
    for n in array:
        answer += str(n) # array에서 뽑아낸 숫자를 문자열로 변환 후 answer에 추가
    return answer.count('7') # answer내 총 7의 개수 리턴하도록
