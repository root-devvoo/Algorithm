# 백준 10250번 ACM 호텔
# https://mungto.tistory.com/341 참고함
T = int(input())

for _ in range(T):
    # H: 호텔의 층 수, W: 각 층의 방 수, N: 몇 번째 손님
    H, W, N = map(int, input().split())
    floor = N % H
    ho = N // H+1
    
    if floor == 0:
        floor = H
        ho -= 1
    # 결과 출력
    print(floor*100 + ho) 
