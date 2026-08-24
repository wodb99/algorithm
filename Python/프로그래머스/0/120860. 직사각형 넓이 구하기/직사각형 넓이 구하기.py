def solution(dots):
    answer = 0
    x_list = []
    y_list = []
    
    for points in dots:
        x, y = points[0], points[1]
        x_list.append(x)
        y_list.append(y)
        
    width = max(x_list) - min(x_list)
    height = max(y_list) - min(y_list)
    
    answer = width * height
    return answer