def solution(nums):
    # 종류의 개수
    types_num = len(set(nums))
    
    if len(nums) / 2 > types_num:
        return types_num
    else:
        return len(nums) / 2
