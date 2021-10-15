import sys
m, n = map(int, sys.stdin.readline().split())

def isprime(m, n):
    # 에라토스테네스의 체
    a = [False,False] + [True]*(n-1)
    primes = []

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    
    # 소수 출력
    for prime in primes:
        if prime >= m: # m 과 같거나 큰 값만...
            print(prime)

# 위에서 정의한 함수 호출
isprime(m, n)
