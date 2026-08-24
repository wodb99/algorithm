def solution(array, n):
    array.sort()
    answer = array[0]
    min_diff = abs(array[0] - n)
    
    for i in array:
        diff = abs(i - n)
        if diff < min_diff:
            min_diff = diff
            answer = i
    
    return answer