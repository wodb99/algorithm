direction = {
    'up': (0, 1),
    'down': (0, -1),
    'left': (-1, 0),
    'right': (1, 0),
}

def solution(keyinput, board):
    answer = []
    
    y, x = 0, 0
    y_end = board[0] // 2
    x_end = board[1] // 2
    
    for direct in keyinput:
        dy, dx = direction[direct]
        if (((y + dy) <= y_end) and ((y + dy) >= -y_end)) and (((x + dx) <= x_end) and ((x + dx) >= -x_end)):
            y += dy
            x += dx
        else:
            continue
            
    answer.append(y)
    answer.append(x)
    
    return answer