# 백준 1181번 단어 정렬
N = int(input())

words = []
for _ in range(N):
    words.append(input())

# 여러 번 입력된 경우에는 한 번씩만 출력하도록 set으로 형변환해서 중복 제거.
set_words = set(words)
# words 리스트를 빈 리스트로 만들어준다.
words.clear()

for w in set_words:
    words.append(w)

# 사전 순으로 정렬
words.sort()
# 길이가 짧은 순으로 정렬
words.sort(key=len)
    
# 결과값 출력    
for word in words:
    print(word)
