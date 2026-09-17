from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):

    # 1. 좌표를 2배로 확대
    rectangle = [
        [x1 * 2, y1 * 2, x2 * 2, y2 * 2]
        for x1, y1, x2, y2 in rectangle
    ]

    # 시작점과 아이템 좌표도 2배
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    # 2. board 생성
    board = [[0] * 102 for _ in range(102)]

    # 3. 모든 사각형의 영역을 1로 채우기
    for x1, y1, x2, y2 in rectangle:
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                board[y][x] = 1

    # 4. 모든 사각형의 내부를 0으로 만들기
    for x1, y1, x2, y2 in rectangle:
        for y in range(y1 + 1, y2):
            for x in range(x1 + 1, x2):
                board[y][x] = 0

    # 5. BFS
    q = deque([(characterX, characterY, 0)])
    visited = [[False] * 102 for _ in range(102)]

    visited[characterY][characterX] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, distance = q.popleft()

        if x == itemX and y == itemY:
            return distance // 2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 102 and 0 <= ny < 102:
                if board[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx, ny, distance + 1))