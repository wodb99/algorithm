def solution(sides):
    answer = 0
    max_v = max(sides)
    min_v = min(sides)
    
    # sides 안의 값이 제일 큰 경우
    for i in range(max_v - min_v + 1, max_v + 1):
        answer += 1
        
    # 새로운 값이 제일 큰 경우:
    for j in range(max_v + 1, max_v + min_v):
        answer += 1
    return answer