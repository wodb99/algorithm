from collections import defaultdict

def solution(array):
    res = defaultdict(int)
    for i in array:
        res[i] += 1
        
    max_v = max(res.values())
    
    modes = []
    for num, cnt in res.items():
        if cnt == max_v:
            modes.append(num)
            
    if len(modes) == 1:
        return modes[0]
    else:
        return -1