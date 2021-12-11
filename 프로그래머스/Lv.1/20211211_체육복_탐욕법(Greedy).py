def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    '''
    여벌의 체육복이 있는 학생이 체육복을 도난 당했을 수 있다는 부분이 있기 때문에
    lost와 reserve에 중복되있는 번호는 제외시켜야한다.
    set은 객체끼리 집합 연산을 지원하므로 차집합을 이용해서 제외를 시켜준다.
    '''
    for reserve_student in reserve_set:
        if reserve_student-1 in lost_set: 
        # 체육복을 빌려줄 수 있는 학생을 기준으로 앞(왼쪽)에 있는 학생이 체육복이 없다면,  
            lost_set.remove(reserve_student-1) 
            # 체육복을 앞(왼쪽)에 있는 학생한테 먼저 빌려주도록 하고,
        elif reserve_student+1 in lost_set: # 뒤(오른쪽)에 있는 학생이 체육복이 없다면
            lost_set.remove(reserve_student+1) # 뒤(오른쪽)에 있는 학생한테 빌려주도록 하고, 잃어버린 학생 집합에서 지운다.
    
    return n - len(lost_set) 
    '''
    체육복이 없는 학생은 체육수업을 들을 수 없다.
    전체 학생 수에서 체육복을 잃어버린 학생들의 수를 빼면,
    체육수업을 들을 수 있는 학생 수가 나온다.
    '''
