from collections import deque

def solution(priorities, location):
    rank = 0
    priorities = deque((v, i) for i, v in enumerate(priorities)) # i or [1] = 문서인덱스, v or [0] = 중요도
    
    while len(priorities):
        document = priorities.popleft() # 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
        
        if priorities and max(priorities)[0] > document[0]: # 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면
            priorities.append(document) # J를 대기목록의 가장 마지막에 넣습니다.
        else: # 3. 그렇지 않으면, J를 인쇄
            rank += 1
            if document[1] == location:
                break
                
    return rank
