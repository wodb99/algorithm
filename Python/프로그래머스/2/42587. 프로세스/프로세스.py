from collections import deque

def solution(priorities, location):
    q = deque((priority, idx) for idx, priority in enumerate(priorities))
    answer = 0
    
    while q:
        current = q.popleft()
        if q and current[0] < max(x[0] for x in q):
            q.append(current)
        else:
            answer += 1
            if current[1] == location:
                return answer