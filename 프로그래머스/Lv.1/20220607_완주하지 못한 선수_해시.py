def solution(participant, completion):
    participant.sort()
    completion.sort()

    for part, comp in zip(participant, completion): 
    # zip : 배열을 같은 인덱스끼리 짝지어줌, 
    #       배열의 길이가 다른 경우 같은 인덱스끼리만 짝지어주고, 나머지 인덱스는 zip객체에서 제외.         
        if part != comp:
            return part
    return participant[-1] # or return participant.pop()
