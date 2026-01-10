from collections import defaultdict

def solution(s):
    answer = ''
    temp = defaultdict(int)
    
    for i in s:
        temp[i] += 1
    
    for j in sorted(temp):
        if temp[j] == 1:
            answer += j
    
    return answer