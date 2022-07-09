# 백준 10250번 ACM 호텔
# https://mungto.tistory.com/341 참고함
T = int(input())

for _ in range(T):
    # H: 호텔의 층 수, W: 각 층의 방 수, N: 몇 번째 손님
    H, W, N = map(int, input().split())
    # 손님이 들어가는 층 수는 N 번째 손님을 높이로 나눈 나머지
    floor = N % H
    # 손님이 들어가는 호실 번호는 N 번째 손님을 높이로 나눈 몫의 +1
    ho = N//H +1
    
    # 높이가 맞아 떨어질 때
    if floor == 0:
        floor = H # 높이를 H로 설정
        ho -= 1 # 호실 번호를 하나 줄임
    # 결과 출력
    print(floor*100 + ho) 
