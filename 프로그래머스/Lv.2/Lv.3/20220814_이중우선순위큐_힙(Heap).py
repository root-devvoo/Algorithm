import heapq

def solution(operations):
    answer = []
    queue = []
    
    for command in operations:
        # I면 I에 해당하는 숫자를 heap에 추가
        if command[0] == "I":
            heapq.heappush(queue, int(command[2:]))
        
        # D인 경우
        elif command[0] == "D":
            # queue에 아무것도 없는 경우
            if not queue:
                continue
            # 공백 뒤가 "-" 일 경우 큐에서 최솟값을 삭제
            elif command[2] == "-":
                heapq.heappop(queue)
            # -가 아닌 경우 최대값 제외
            else:
                queue = heapq.nlargest(len(queue), queue)[1:]
                heapq.heapify(queue)

    ## 최종 결과 출력
    if queue:
        answer.append(max(queue))
        answer.append(min(queue))
    # 큐가 비어있는 경우 0으로 채움
    else:
        answer.append(0)
        answer.append(0)

    return answer
