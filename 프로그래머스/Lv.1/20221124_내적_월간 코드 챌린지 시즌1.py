def solution(a, b):
    answer = 0
    
    n = len(a)
    for idx in range(n):
        answer += a[idx]*b[idx]
        
    return answer
