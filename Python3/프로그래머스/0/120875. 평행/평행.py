def solution(dots):
    cases = [
        (0, 1, 2, 3),
        (0, 2, 1, 3),
        (0, 3, 1, 2)
    ]
    
    for a, b, c, d in cases:
        dy1 = dots[b][1] - dots[a][1]
        dx1 = dots[b][0] - dots[a][0]
        dy2 = dots[d][1] - dots[c][1]
        dx2 = dots[d][0] - dots[c][0]
        
        if dy1 * dx2 == dy2 * dx1:
            return 1
            
    return 0
