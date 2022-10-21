# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.8.10
    return len(max(bin(N)[2:].strip('0').strip('1').split('1')))
