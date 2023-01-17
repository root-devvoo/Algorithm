def solution(arr):
  length = 1 # 길이가 2 이상인 증가하는 구간이 없는 경우 1을 return해야하므로
  max_length = 1  # 모든 길이 카운트는 1부터 시작하도록 한다.
  tmp = 0
  for n in arr:
    # 연속해서 증가하는 경우
    if tmp < n: # (바로 전 숫자와 현재 숫자가 같은 경우는 증가한 것으로 보지 않으므로, n은 무조건 tmp보다 커야함)
      length += 1 # 길이 1 증가
    else: # 연속해서 증가하지 않는 경우
      if length > max_length: # 현재까지 연속 증가된 길이가 max_length보다 크면,
        max_length = length # 현재까지 연속 증가된 길이를 max_length로 덮어씌움.
      length = 1 # 연속이 깨졌으므로, length는 1로 다시 초기화
    
    tmp = n # 다음 숫자와 연속해서 증가하는지를 비교하기 위해 n을 tmp 변수에 덮어 씌워줌. 
    
  return max_length # 숫자가 연속해서 증가하는 가장 긴 구간의 길이 return

########################################################################################################
arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")