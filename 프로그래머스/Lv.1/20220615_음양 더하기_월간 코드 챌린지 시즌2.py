def solution(absolutes, signs):
    result = 0
    
    for i in range(len(absolutes)):
        # signs[i]가 참이면, absolutes[i]의 실제 정수는 양수
        if signs[i] == True:
            result += absolutes[i]
        # 그렇지 않으면, 음수    
        else:
            result -= absolutes[i]
            
    return result
