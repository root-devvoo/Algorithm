def solution(sizes):
    width = []
    height = []
    
    for i in range(len(sizes)):
        # 가로 길이가 세로 길이보다 더 긴 경우는 그대로 사용하기 위해서 
        if sizes[i][0] >= sizes[i][1]:
            # 값들을 그대로해서 width 리스트에 넣는다.
            width.append(sizes[i][0])
            height.append(sizes[i][1])
        # 세로 길이가 더 긴 경우는 가로로 눕혀 넣게 하기 위해서  
        else:
            # 값을 뒤집어 height 리스트에 넣는다.
            height.append(sizes[i][0])
            width.append(sizes[i][1])
            
    # width, heigth 각 리스트의 최댓값끼리 곱하여 최종 지갑 넓이 결과를 추출
    return max(width) * max(height)
