def solution(lines):
    answer = 0
    visited = [0] * 200
    
    for start, end in lines:
        for i in range(start, end):
            visited[i + 100] += 1
            
    for j in visited:
        if j >= 2:
            answer += 1
            
    return answer