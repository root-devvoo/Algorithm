word = input().lower()
word_sum = list(set(word)) # set 으로 변환해서 중복 제거 후 리스트로
cnt_alphabet = []

for s in word_sum:
    cnt_alphabet.append(word.count(s))
# 중복을 제거시킨 리스트 안에 있는 요소를 s라는 변수로 뽑아서
# 맨 처음에 받았던 원래 word 단어... 알파벳 요소들의 개수를 세고
# cnt_alphabet 리스트에 개수 센 값을 넣어 줌

# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력
if cnt_alphabet.count(max(cnt_alphabet)) > 1:
    print('?')

# 맨 처음에 받았던 단어에서 가장 많이 사용된 알파벳을 대문자로 출력
else: # (가장 사용 개수가 많은 알파벳 index를 토대로 word_sum 리스트에서 가장 많이 사용한 알파벳을 가져오도록 구현함)
    print(word_sum[cnt_alphabet.index(max(cnt_alphabet))].upper())
