def solution(array, commands):
    answer = [(sorted(array[i-1:j]))[k-1] for i, j, k in commands]
    # 인덱스는 0부터 시작이므로 -1 해줘야 함
    return answer
