def solution(common):
    answer = 0
    flag = 0
    
    if (common[2] - common[1]) == (common[1] - common[0]):
        flag = 1
        
    if flag:
        d = common[1] - common[0]
        answer = common[0] + len(common) * d
    else:
        r = common[1] / common[0]
        answer = common[0] * (r ** len(common))
        
    return answer