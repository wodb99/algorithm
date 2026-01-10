def solution(i, j, k):
    answer = 0
    k = str(k)
    
    for num in range(i, j+1):
        answer += str(num).count(k)
    return answer