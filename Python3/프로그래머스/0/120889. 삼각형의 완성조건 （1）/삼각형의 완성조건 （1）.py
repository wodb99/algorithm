def solution(sides):
    answer = 0
    sides.sort()
    max_v = sides[-1]
    val = sides[0] + sides[1]
    if val > max_v:
        answer = 1
    else:
        answer = 2
    return answer