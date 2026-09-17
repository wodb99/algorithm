from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    
    q = deque([(0, 0, 1)]) # (시작 행, 시작 열, 현재까지 이동 거리)
    visited = set([(0, 0)])
    
    while q:
        y, x, dist = q.popleft()
        
        if (y, x) == (n-1, m-1):
            return dist
    
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1 and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    q.append((ny, nx, dist + 1))
                    
    return -1