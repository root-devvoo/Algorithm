def solution(commands):
  answer = [0, 0]
  heading = {'L':[-1, 0], 'R':[1, 0], 'U':[0, 1], 'D':[0, -1]}
  
  for k in commands:
    answer[0] += heading[k][0]
    answer[1] += heading[k][1]
  
  return answer
#####################################################################
commands = "URDDL"
ret = solution(commands)

print("solution 함수의 반환 값은", ret, "입니다.")