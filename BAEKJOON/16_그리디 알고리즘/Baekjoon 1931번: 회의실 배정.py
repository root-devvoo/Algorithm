n = int(input()) # 회의의 수

meeting_time = []

for _ in range(n):
    start, end = map(int, input().split())
    meeting_time.append((start, end)) # 힌트 참고

meeting_time.sort(key=lambda m: (m[1], m[0])) # 회의가 끝나는 시간 순으로 정렬
# key 파라미터 : 정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.
# 그러면, key 값을 기준으로 정렬된다. (오름차순이 Default)
  
count = 1 # 맨 첫 회의는 비어있기 때문에 무조건 가능하므로 1부터 시작한다.

end_time = meeting_time[0][1] # 진행중인 회의가 끝나는 시간을 end_time 변수에 지정

for i in range(1, n):
    if meeting_time[i][0] >= end_time:
    # 잡으려고 하는 회의 시작 시간이 이미 진행하고 있는 회의가 끝나는 시간과 같거나 그 이후면
        # 새로 잡는 회의의 끝나는 시간으로 end_time 변수에 덮고    
        end_time = meeting_time[i][1] 
        count += 1 # 카운트를 1 올려준다.

print(count)
