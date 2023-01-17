# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(password): # cba323
  length = len(password) # length = 6
  for i in range(length - 2): # i = 0, 1, 2, 3
    first_check = ord(password[i + 1]) - ord(password[i]) # b(98)-c(99) = -1
    second_check = ord(password[i+2]) - ord(password[i+1]) #  a(97)-b(98) = 1 !!! 바꾼 부분
    if first_check == second_check and (first_check == 1 or first_check == -1):
      return False # 연속된 것
  return True
##########################################################################################
password1 = "cospro890"
ret1 = solution(password1)

print("solution 함수의 반환 값은", ret1, "입니다.")

password2 = "cba323"
ret2 = solution(password2)

print("solution 함수의 반환 값은", ret2, "입니다.")  