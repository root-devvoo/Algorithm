import sys # 속도 해결을 위한 sys 모듈 import

stack = []

# 정수 x를 스택에 넣는 연산
def push(x):
    stack.append(x)
    
# 스택에서 가장 뒤에 있는 정수를 삭제
# 만약 스택에 들어있는 정수가 없는 경우에는 -1 출력
def pop():
    if not stack:
        print(-1) 
    else:
        del stack[-1]
#########################################################
n = int(sys.stdin.readline()) # 명령의 수

for _ in range(n):
    command = sys.stdin.readline().split() # split해서 입력받기 : push 1 같은 애들을 분리하기 위해서...
    order = command[0] # 명령될 함수 받기
    
    if order == '0':
        pop()
    
    else:
        push(int(command[0]))
    
if len(stack) == 0:
    print(0)
else:
    print(sum(s for s in stack))
