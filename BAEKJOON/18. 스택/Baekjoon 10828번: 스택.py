import sys # 속도 해결을 위한 sys 모듈 import

stack = []

# 정수 x를 스택에 넣는 연산
def push(x):
    stack.append(x)
    
# 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력
# 만약 스택에 들어있는 정수가 없는 경우에는 -1 출력
def pop():
    if not stack:
        print(-1) 
    else:
        print(stack.pop())
   
# 스택에 들어있는 정수의 개수를 출력한다.
def size():
    print(len(stack))
    
# 스택이 비어있으면 1, 아니면 0을 출력한다.
def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)
   
# 스택의 가장 위에 있는 정수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1 출력
def top():
    if len(stack) != 0:
        print(stack[-1])
    else:
        print(-1)

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
    elif order == 'top':
        top()      
