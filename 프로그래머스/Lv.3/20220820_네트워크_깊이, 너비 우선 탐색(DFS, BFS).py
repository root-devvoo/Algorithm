def solution(n, computers):
    answer = 0
    
    root = [i for i in range(n)]
    
    ######################### 유니온 파인드 구현 #########################
    # 같은 트리 내 모든 노드의 부모를 루트 노드로 가리키게 하는 find 함수
    def find(target):
        if root[target] == target: # 루트 노드는 자기 자신을 부모 노드로 가리킨다.
            return target
        else:
            # 각 노드의 부모 노드를 찾아 올라간다.
            root[target] = find(root[target])
            return root[target]
    
    # 각 원소가 속한 트리의 루트 노드를 찾는 union 함수
    def union(x, y):
        x = find(x)
        y = find(y)
    
        root[y] = x
    
        return answer
    ##################################################################
    # computers 배열을 돌면서 연결되어 있는 경우 부모를 찾아낸다.
    for i in range(n):
        for j in range(n):
            # 자기 자신을 가리키거나, 연결된 상태가 아닐 때는
            if i == j or computers[i][j] == 0: 
                continue # continue문으로 union을 하지 않게 하면,
            union(i, j) # 자기 자신을 가리키지 않으면서, 연결된 상태인 것에 대해서만
            # union 함수로 부모 노드를 찾음 
    
    # 예외 처리 (?)
    for i in range(n):
        root[i] = find(i)
    
    answer = len(set(root))
    # 최종 결과 리턴
    return answer   
