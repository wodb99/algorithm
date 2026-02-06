from collections import defaultdict

def solution(nums):
    answer = 0
    pocket = defaultdict(int)
    
    for i in nums:
        pocket[i] += 1
        
    cnt = len(pocket.keys())
    
    if cnt <= (len(nums) / 2):
        answer = cnt
    else:
        answer = len(nums) / 2
        
    return answer