def solution(num, k):
    temp = list(str(num))
    if str(k) in temp:
        return temp.index(str(k)) + 1
    else:
        return -1