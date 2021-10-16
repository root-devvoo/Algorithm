# 재귀함수를 이용한 풀이
import sys

n = int(sys.stdin.readline())

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(n))
