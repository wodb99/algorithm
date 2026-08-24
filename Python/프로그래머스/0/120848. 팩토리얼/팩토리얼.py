def solution(n):
    answer = 0
    res = 1
    
    for i in range(1, 11):
        res *= i
        if res <= n:
            answer = i
    return answer