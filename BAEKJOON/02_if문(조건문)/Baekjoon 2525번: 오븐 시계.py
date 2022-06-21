# 백준 2525번 오븐 시계

# (1) 현재 시각
# 연산을 위해 현지 시각의 시간과 분을 나눠 입력받음
current_hour, current_min = map(int, input().split())
# (2) 요리하는 데 필요한 시간 (분 단위)
cooking_min = int(input())

# 연산
current_hour += (cooking_min // 60)
current_min += (cooking_min % 60)
# 만약, 분이 60 이상이면
if current_min >= 60:
    current_hour += 1 # 시간을 1 더해주고,
    current_min -= 60 # 분에서 60를 뺌
    
# 시간이 24 이상이면,
if current_hour >= 24:
    current_hour -= 24 # 시간에서 24 뺌
        
# 결과 리턴
print(str(current_hour) + ' ' + str(current_min))    
