str = input()
answer = ''

for s in str:
    if s.islower() == True:
        answer += s.upper()
    else:
        answer += s.lower()

print(answer)
