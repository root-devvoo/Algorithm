def solution(lottos, win_nums):
    answer = 0
    zero = lottos.count(0)
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    # 그 외 6등, 2개 번호 일치 5등, 3개 번호 일치 4등 이와 같은 식으로 딕셔너리로 순위 지정
    
    for _ in lottos:
        if _ in win_nums:
            answer += 1
    
    answer_max = answer + zero # 0이 다 맞았을 경우 가정
    answer_min = answer # 0이 다 틀렸을 경우 가정
    
    return [rank[answer_max], rank[answer_min]]
