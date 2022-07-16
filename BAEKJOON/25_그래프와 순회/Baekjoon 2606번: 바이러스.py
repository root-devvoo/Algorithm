# 백준 2606 바이러스
# 첫째 줄 : 컴퓨터의 수
com_num = int(input())
# 둘째 줄 : 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수 (간선의 수)
pair_num = int(input())
network = {}

# 딕셔너리로 network 그래프 만들기
for i in range(pair_num): # 쌍의 수 만큼 그래프가 구현되어야 함
    a, b = map(int, input().split())
    # a라는 수를 가진 노드가 network 그래프에 있으면, 
    if a in network:
        # a에다가 b값을 넣어준다.
        network[a].add(b)
    else: # a라는 수를 가진 노드가 network 그래프에 없으면,
        network[a] = set([b]) # a라는 노드를 만든 후 거기에 set형식으로 b값을 넣어준다.     
    
    # b라는 수를 가진 노드가 network 그래프에 있으면
    if b in network:
        # b에다가 a값을 넣어준다.
        network[b].add(a)
    else: # b라는 수를 가진 노드가 network 그래프에 없으면,
        network[b] = set([a]) # b라는 노드를 만든 후 거기에 set형식으로 a값을 넣어준다.  

## DFS(깊이우선탐색) 하는 함수 기능 구현
# (참고 링크 : https://data-marketing-bk.tistory.com/44)
def dfs(graph, start_node):
    # 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visit, visited = list(), list()
    # 시작 노드를 지정하기 
    need_visit.append(start_node)
    # 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visit:
        # 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visit.pop()
        # 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
            # 방문한 목록에 추가하기 
            visited.append(node)
            # 그리고, 인접 노드들을 방문 예정 리스트에 추가 
            need_visit.extend(graph[node])
    # dfs 시작 노드에 해당하는 1개 노드에 대해서는 차감해서 리턴         
    return len(visited) - 1

# 바이러스 최종 결과 출력
print(dfs(network, 1))
