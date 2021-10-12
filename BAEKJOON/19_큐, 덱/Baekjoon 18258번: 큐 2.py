import sys

from collections import deque
# deque는 스택과 큐의 기능을 모두 가진 객체로 출입구를 양쪽에 가지고 있다
# 스택처럼 써도 되고, 큐처럼 써도 된다.

queue = deque()
# list로 선언해서 pop(0)를 하게 되면,
# 첫 번째 element를 pop 하고나서 나머지 element들의 인덱스를
# 1칸씩 당기는 과정에서 O(n)의 계산량이 발생한다.
# 따라서 deque를 이용한다.
# 출처 :: https://www.acmicpc.net/board/view/47845

# 정수 x를 큐에 넣는 연산
def push(x):
    queue.append(x)
    
# 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력
# 만약 큐에 들어있는 정수가 없는 경우 -1 출력
def pop():
    if len(queue) == 0:
        print(-1) 
    else:
        print(queue[0])
        queue.popleft() # deque 쓸 경우 :: 왼쪽에서 값을 빼고 싶으면 popleft()를 사용한다.     

# 큐에 들어있는 정수의 개수를 출력한다
def size():
    print(len(queue))

# 큐가 비어있으면 1, 아니면 0을 출력한다
def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)

# 큐의 가장 앞에 있는 정수를 출력한다
# 만약 큐에 들어있는 정수가 없는 경우 -1 출력
def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

# 큐에 가장 뒤에 있는 정수를 출력한다
# 만약 큐에 들어있는 정수가 없는 경우 -1 출력
def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])
        
n = int(sys.stdin.readline()) # 명령의 수

for _ in range(n):
    command = sys.stdin.readline().split() # split해서 입력받기 : push 1 같은 애들을 분리하기 위해서...
    order = command[0] # 명령될 함수 받기
    
    # order에 따라 정의된 함수기능 수행
    if order == "push":
        push(command[1])
    elif order == 'pop':
        pop()
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    elif order == 'front':
        front()
    elif order == 'back':
        back()
