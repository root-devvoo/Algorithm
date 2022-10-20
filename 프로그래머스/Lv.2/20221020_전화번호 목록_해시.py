def solution(phone_book):
    answer = True
    
    # 짧은 단어부터 접두사를 비교, 확인하기 위해서 정렬
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
                   answer = False
    
    return answer
