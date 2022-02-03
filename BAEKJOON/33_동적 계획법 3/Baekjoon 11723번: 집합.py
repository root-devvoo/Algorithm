# 백준 11723번 집합
import sys

S = set()
# 집합 연산 함수 정의
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) 
# S에 x가 이미 있는 경우에는 연산을 무시한다.
def add(x):
    S.add(x)
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) 
# S에 x가 없는 경우에는 연산을 무시한다.
def remove(x):
    S.discard(x) # discard()는 엘레먼트가 없어도 정상종료함.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
def check(x):
    if x in S:
        print(1)
    else:
        print(0)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
def toggle(x):
    if x in S:
        S.discard(x) # discard()는 엘레먼트가 없어도 정상종료함.
    else:
        S.add(x)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
def all():
    global S
    S = set([i for i in range(1, 21)]) # 이렇게 해야 시간 초과 안됨                                 
# empty: S를 공집합으로 바꾼다.
def empty():
    S.clear()    
####################################################################################
# 첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
M = int(sys.stdin.readline()) 
# 둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.
for _ in range(M):
    command = sys.stdin.readline().split()
    order = command[0]
    # indexerror 해결을 위해서 command 길이에 따른 조건으로 분리
    if len(command) == 1:
        # order에 따라 정의된 함수기능 수행
        if order == 'all':
            all()
        elif order == 'empty':
            empty()             
            
    else:
        x = int(command[1])
        # order에 따라 정의된 함수기능 수행
        if order == 'add':
            add(x)
        elif order == 'remove':
            remove(x)
        elif order == 'check':
            check(x)
        elif order == 'toggle':
            toggle(x)
