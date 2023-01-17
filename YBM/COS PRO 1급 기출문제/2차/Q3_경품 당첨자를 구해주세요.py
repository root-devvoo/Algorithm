# n = 3 => 1000
# n = 2 => 100
def func_a(n):
  ret = 1 # 1 -> 10 -> 100 -> 1000 ...
  while n > 0:
    ret *= 10
    n -= 1
  return ret

# n => 367, 36, 3, 0
# ret = 0, 1, 2, 3
# n의 자릿수를 반환하는 함수
def func_b(n):
  ret = 0
  while n > 0:
    ret += 1
    n //= 10
  return ret

# n => 367, 36, 3, 0
# ret => 0+7+6+3
# n의 각 자릿수 합을 구해 반환하는 함수
def func_c(n):
  ret = 0
  while n > 0:
    ret += n%10
    n //= 10
  return ret
############################################################################
def solution(num):
  next_num = num
  while True: 
    next_num += 1 # 1. 게시글 번호를 1 증가시키고 자릿수를 구합니다.
    length = func_b(next_num) # 빈칸
    if length % 2: # 2. 만약 자릿수가 짝수가 아니라면 1로 돌아갑니다.
      continue
    # 자릿수가 짝수인 경우
    divisor = func_a(length//2) # 빈칸, 123456 -> length//2 => 3 (1000)
    front = next_num // divisor # 123456//1000 == 123 (앞의 세자리)
    back = next_num % divisor # 123456%1000 == 456 (뒤의 세자리)

    front_sum = func_c(front) # 빈칸
    back_sum = func_c(back) # 빈칸
    if front_sum == back_sum:
      break
  return next_num - num
############################################################################
num1 = 1
ret1 = solution(num1)

print("solution 함수의 반환 값은", ret1, "입니다.")

num2 = 235386
ret2 = solution(num2)

print("solution 함수의 반환 값은", ret2, "입니다.")