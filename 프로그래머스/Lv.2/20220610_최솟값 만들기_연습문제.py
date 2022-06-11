def solution(A,B):
    answer = 0
    
    # 모든 조합의 곱들의 최종 누적된 값이 최소가 되도록
    A.sort() # A 배열에서는 가장 작은 값부터 (오름차순),
    B.sort(reverse=True) # 다른 B 배열에서는 가장 큰 값부터 조합하도록 정렬함 (내림차순) (반대로 해도 상관없을듯)

    for a, b in zip(A, B):
        answer = answer + (a * b)
        
    return answer
