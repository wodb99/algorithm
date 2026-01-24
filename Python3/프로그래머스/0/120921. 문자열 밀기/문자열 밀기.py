def solution(A, B):
    if A == B:
        return 0
    
    temp = A
    for cnt in range(1, len(A)):
        temp = temp[-1] + temp[:-1]
        if temp == B:
            return cnt
            
    return -1