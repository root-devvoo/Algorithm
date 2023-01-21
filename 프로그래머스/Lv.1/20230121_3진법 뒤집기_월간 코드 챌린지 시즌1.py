def solution(n):
    answer = ''
   
    while n >= 1:
        n, remainder = divmod(n, 3)  # divmod(): 몫과 나머지를 같이 반환해주는 함수
        # 10진수를 n진수로 바꾸는 방법은 바꾸고자하는 10진수의 정수를 n으로 몫이 0이 될 때까지 나누고, 나머지를 아래방향부터 읽으면 됨.
        # print(n, remainder)
        answer += str(remainder) # 그러므로, 맨 처음에 나온 나머지부터 answer에 넣어줌
    
    return int(answer, 3) # 그리고, 앞뒤 반전 3진수 -> 10진수로 변환
