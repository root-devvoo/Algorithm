def solution(array):
    answer = []
    
    max_num = max(array)
    idx_num = array.index(max_num)
    
    answer.append(max_num)
    answer.append(idx_num)
    return answer
