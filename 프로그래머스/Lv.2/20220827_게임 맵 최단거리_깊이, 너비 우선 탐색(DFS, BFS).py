# 이것이 취업을 위한 코딩 테스트다 with 파이썬 - 나동빈 저
# 책에 수록된 미로 탈출 문제 풀이를 참고해서 풀었다.

from collections import deque

def solution(maps):
    answer = 0
    
    # 이동할 네 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    len_x = len(maps)
    len_y = len(maps[0])   
    
    ## BFS 기능 구현
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            # 현재 위치에서 네 방향으로의 위치 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵 공간을 벗어난 경우 무시
                if nx < 0 or ny < 0 or nx >= len_x or ny >= len_y:
                    continue

                # 벽인 경우 무시
                if maps[nx][ny] == 0:
                    continue

                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    
        # 가장 오른쪽 아래까지의 (상대팀 진영까지의) 최단 거리 값 반환
        return maps[len_x - 1][len_y - 1]
    
    ### 최종 결과 출력
    answer = bfs(0, 0)
    # 상대 팀 진영에 도착할 수 없을 때는 -1을 반환
    if answer == 1:
        return -1
    else:
        return answer
