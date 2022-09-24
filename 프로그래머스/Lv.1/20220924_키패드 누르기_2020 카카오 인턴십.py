def solution(numbers, hand):
    answer = ''
    
    # 키패드를 dictionary 좌표로 구현
    keypad = { 1: [0, 0], 2: [0, 1], 3: [0, 2],
               4: [1, 0], 5: [1, 1], 6: [1, 2],
               7: [2, 0], 8: [2, 1], 9: [2, 2],
               '*': [3, 0], 0: [3, 1], '#': [3, 2]
             }
    
    # 시작 위치 셋팅
    left_h = keypad['*']
    right_h = keypad['#']
    
    for i in numbers:
        now = keypad[i]
        # 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
        if i in [1, 4, 7]:
            answer += 'L'
            left_h = now
        
        # 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
        elif i in [3, 6, 9]:
            answer += 'R'
            right_h = now
        
        # 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 
        # 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
        else:
            left_loc = 0
            right_loc = 0

            # 좌표 거리 계산 (각 손 위치 좌표 - 현재위치 좌표)
            for lh, rh, n in zip(left_h, right_h, now):
                left_loc += abs(lh-n)  
                right_loc += abs(rh-n)

            # 왼손이 더 가까우면
            if left_loc < right_loc:
                answer += 'L'
                left_h = now
            # 오른손이 더 가까우면    
            elif left_loc > right_loc:
                answer += 'R'
                right_h = now
                
            # 4-1 만약 두 엄지손가락의 거리가 같다면, 
            # 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
            else:
                # 오른손잡이
                if hand == 'right':
                    answer += 'R'
                    right_h = now
                # 왼손잡이
                else:
                    answer += 'L'
                    left_h = now
    # 최종 결과 출력
    return answer
