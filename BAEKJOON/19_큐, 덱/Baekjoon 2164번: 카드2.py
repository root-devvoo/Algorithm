# deque를 활용한 풀이
from collections import deque

N = int(input())
queue = deque([i+1 for i in range(N)])

while len(queue) > 1:
    queue.popleft()
    temp = queue.popleft()
    queue.append(temp)

print(queue.pop()) # 마지막 남은 카드 숫자를 알기 위해 pop() 사용
