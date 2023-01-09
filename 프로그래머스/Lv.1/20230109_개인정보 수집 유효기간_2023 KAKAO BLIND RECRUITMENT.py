def solution(today, terms, privacies):
    answer = []
    
    # today를 연, 월, 일을 나눈 뒤 일수로 변환
    year, month, day = today.split('.')
    today = int(year)*12*28 + int(month)*28 + int(day)
    # 약관 종류별로 일수로 치환해서 딕셔너리에 추가
    terms = { term[:1] : int(term[2:])*28 for term in terms } # K = 약관 종류, V = 유효기간(일수)
    
    for idx, privacy in enumerate(privacies):
        # 개인정보 수집 일자를 연, 월, 일로 나눔
        year, month, day = privacy.split('.')
        # 이대로 day를 사용하면, 약관 종류까지 같이 나오므로 한번 더 분리해줌
        day, t_type = day.split()
        # 일수로 변환
        privacy = int(year)*12*28 + int(month)*28 + int(day)
        # (개인정보 수집 일자 + 약관 종류에 따른 유효기간) 값이 today값보다 적거나 같은 경우
        if privacy+terms[t_type] <= today: # 유효기간이 지나 파기 해야함
            answer.append(idx+1) # 그러므로, 정답 리스트에 인덱스+1 해서 추가
            
    return answer
