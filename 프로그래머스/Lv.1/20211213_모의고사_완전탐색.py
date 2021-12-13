def solution(answers):
    # 수포자 삼인방의 문제 찍는 방식 리스트 정의
    supoja1 = [1,2,3,4,5]
    supoja2 = [2,1,2,3,2,4,2,5]
    supoja3 = [3,3,1,1,2,2,4,4,5,5]
    # 수포자 삼인방의 점수를 담을 리스트
    score = [0,0,0]
    
    # 정답 비교해서 점수 계산
    for i in range(len(answers)):
        if answers[i] == supoja1[i%5]:
            score[0] += 1
        if answers[i] == supoja2[i%8]:
            score[1] += 1
        if answers[i] == supoja3[i%10]:
            score[2] += 1
    # 높은 점수를 받은 사람 출력하기
    max_score = max(score)
    return [i+1 for i, score in enumerate(score) if max_score == score]
