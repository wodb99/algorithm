def solution(a, b):
    val1 = int(str(a) + str(b))
    val2 = 2 * a * b
    
    return max(val1, val2)