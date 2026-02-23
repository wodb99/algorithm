from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer

# 제대로 이해안가지만 시간 복잡도 더 좋음
# def solution(prices):
#     n = len(prices)
#     answer = [0] * n
#     stack = []
    
#     for i in range(n):
        
#         # 현재 가격이 더 작으면 → 떨어진 것
#         while stack and prices[stack[-1]] > prices[i]:
#             top = stack.pop()
#             answer[top] = i - top
        
#         stack.append(i)
    
#     # 끝까지 안 떨어진 애들 처리
#     while stack:
#         top = stack.pop()
#         answer[top] = n - 1 - top
        
#     return answer