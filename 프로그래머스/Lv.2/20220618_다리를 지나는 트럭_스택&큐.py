def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 다리 길이 만큼 0 채워서 다리 리스트 정의
    bridge = [0 for _ in range(bridge_length)]
    # bridge 리스트의 길이가 0이 아닐때만 while문 반복
    while bridge:
        
        answer += 1 # 시간 더하기
        bridge.pop(0)
        
        if len(truck_weights) > 0: # 트럭 대기 리스트의 길이가 0이 아닐 때까지 반복!
            # 다리 위에 있는 트럭들의 무게 합과 대기중인 다음 차례의 트럭 무게가 조건을 만족할 시
            if (sum(bridge) + truck_weights[0]) <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck) # 다리 리스트에 추가
            else: # 만족 못할 시
                bridge.append(0) # 0을 추가해서 다리의 길이 유지
        
    return answer
