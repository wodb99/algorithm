from collections import defaultdict

def solution(nums):
    temp = defaultdict(int)
    for i in nums:
        temp[i] += 1
    cnt = len(temp.keys())
    val = len(nums) // 2
    if val < cnt:
        return val
    return cnt