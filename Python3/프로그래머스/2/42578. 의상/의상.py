from collections import defaultdict

def solution(clothes):
    answer = 1
    cloth = defaultdict(list)
    
    for name, typ in clothes:
        cloth[typ].append(name)
        
    for typ in cloth:
        answer *= (len(cloth[typ]) + 1) # 각 하나 선택 or 안 입음
        
    return answer - 1 # 아무것도 안 입는 경우 하나 빼기