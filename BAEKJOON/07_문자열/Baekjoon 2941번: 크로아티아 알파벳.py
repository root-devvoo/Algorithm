alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()

for alphabet in alphabets:
    # 문자열 안에 alphabets로 정의된 단어가 있다면, 한 글자로 처리하게끔 기호로 바꿔줌
    str = str.replace(alphabet, '#')

print(len(str))    
