def solution(k, score):
    answer = []
    HOF = [] # 명예의 전당
    
    for s in score:
        HOF.append(s)
        HOF.sort(reverse=True) # 내림차순 정렬
        # 명예의 전당 사이즈가 k를 초과해버리면 
        if len(HOF) > k:
            HOF.pop() # 맨 뒤 숫자 날림
        
        answer.append(HOF[-1]) # 명예의 전당에서 최소 숫자 answer에 추가
    
    return answer
