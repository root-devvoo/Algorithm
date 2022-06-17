def solution(progresses, speeds):
    answer = []
    
    while progresses: # progresses 다 될 때까지 while문으로 반복
        # progresses length 만큼 for문 반복해서 기능 진행 업데이트
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        count = 0
        # 100까지 완성된 기능 순차적 배포하고, count 1 증가
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        # 특정일 100으로 배포한 개수가 0보다 클 경우 answer에 append
        if count > 0:
            answer.append(count)
    
    return answer
