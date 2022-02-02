# 백준 10866: 덱
import sys
from collections import deque

deq = deque()

# 덱 함수들 정의
# push_front X: 정수 X를 덱의 앞에 넣는다.
def push_front(x):
    deq.appendleft(x)

# push_back X: 정수 X를 덱의 뒤에 넣는다.
def push_back(x):
    deq.append(x)

# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 
# 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop_front():
    if len(deq) == 0:
        print(-1)
    else:
        print(deq[0])
        deq.popleft()

# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 
# 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop_back():
    if len(deq) == 0:
        print(-1)
    else:
        print(deq[-1])
        deq.pop()

# size: 덱에 들어있는 정수의 개수를 출력한다.
def size():
    print(len(deq))

# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
def empty():
    if len(deq) == 0:
        print(1)
    else:
        print(0)

# front: 덱의 가장 앞에 있는 정수를 출력한다.
# 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def front():
    if len(deq) == 0:
        print(-1)
    else:
        print(deq[0])

# back: 덱의 가장 뒤에 있는 정수를 출력한다. 
# 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def back():
    if len(deq) == 0:
        print(-1)
    else:
        print(deq[-1])
#########################################################################################
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다.
N = int(sys.stdin.readline())
for _ in range(N):
    command = sys.stdin.readline().split() # split해서 입력받기 : push_front X 형식으로 분리하기 위해서...
    order = command[0]

    # order에 따라 정의된 함수기능 수행    
    if order == "push_front":
        push_front(command[1])
    elif order == 'push_back':
        push_back(command[1])
    elif order == 'pop_front':
        pop_front()
    elif order == 'pop_back':
        pop_back()
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    elif order == 'front':
        front()
    elif order == 'back':
        back()                                                                                         
