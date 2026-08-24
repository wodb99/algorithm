def solution(array):
    answer = []
    val = max(array)
    answer.append(val)
    idx = array.index(val)
    answer.append(idx)
    return answer