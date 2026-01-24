# def solution(A, B):
#     if A == B:
#         return 0
    
#     temp = A
#     for cnt in range(1, len(A)):
#         temp = temp[-1] + temp[:-1]
#         if temp == B:
#             return cnt
            
#     return -1

from collections import deque

def solution(A, B):
    a, b = deque(A), deque(B)
    
    for cnt in range(0, len(A)):
        if a == b:
            return cnt
        a.rotate(1)
    
    return -1
