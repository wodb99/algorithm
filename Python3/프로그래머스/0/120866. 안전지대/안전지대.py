directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def bomb(y, x, visited, n):
    visited[y][x] = 1
    
    for dy, dx in directions:
        ny = y + dy
        nx = x + dx
        
        if 0 <= ny < n and 0 <= nx < n:
            visited[ny][nx] = 1

def solution(board):
    answer = 0
    n = len(board)
    visited = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bomb(i, j, visited, n)
                
    for k in range(n):
        for l in range(n):
            if visited[k][l] == 0:
                answer += 1
                
    return answer