from collections import deque

def solution(priorities, location):
    answer = []
    queue = deque((i, j) for i, j in enumerate(priorities)) # 인덱스와 같이 저장
    
    while queue:
        process = queue.popleft()
        if queue and any(process[1] < q[1] for q in queue): # 우선순위가 큰 게 하나라도 존재한다면 다시 큐에 집어넣음
            queue.append(process)
        else:
            answer.append(process)
        
    for i in answer:
        if i[0] == location:
            return answer.index(i) + 1