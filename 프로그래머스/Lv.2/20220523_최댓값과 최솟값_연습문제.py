def solution(s):
    numbers = list(map(int, s.split(" "))) # 공백 기준으로 나눠서 int형의 리스트로 만듬
    return str(min(numbers)) + " " + str(max(numbers)) # 리스트 안에서 최댓값, 최솟값을 찾아 제시한 결과값 형식에 맞게 string 타입으로 만들어 리턴
