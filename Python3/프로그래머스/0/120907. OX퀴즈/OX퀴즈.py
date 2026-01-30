# def solution(quiz):
#     answer = []
#     for i in quiz:
#         if eval(i.split('=')[0]) == int(i.split('=')[1]):
#             answer.append('O')
#         else:
#             answer.append('X')
#     return answer

def solution(quiz):
    answer = []
    
    for i in quiz:
        left, right = i.split('=')
        right = int(right)
        
        a, op, b = left.split()
        a, b = int(a), int(b)
        
        if op == '+':
            result = a + b
        else:
            result = a - b
            
        if result == right:
            answer.append('O')
        else:
            answer.append('X')
            
    return answer