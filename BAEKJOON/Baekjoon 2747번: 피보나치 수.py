# 동적계획법 Bottom up 방식으로 접근한 풀이
import sys

n = int(sys.stdin.readline())

def fib(n):
    fibList = [0, 1]
    for i in range(2, n+1):
        fibList.append(fibList[i-2] + fibList[i-1])
    return fibList[-1]

print(fib(n))
