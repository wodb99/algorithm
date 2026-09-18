def solution(tickets):
    tickets.sort()
    used = [0] * len(tickets)
    path = ["ICN"]
    
    def dfs(current):
        if len(path) == len(tickets) + 1:
            return True
        
        for i in range(len(tickets)):
            if used[i]:
                continue
            
            start, end = tickets[i]
            if start != current:
                continue
            
            used[i] = 1
            path.append(end)
            
            if dfs(end):
                return True # 현재 공항에서 출발할 수 있는 경로 X
            
            path.pop() # 추가한 경로 제거
            used[i] = 0 # 티켓 사용 취소
        
        return False
    
    dfs("ICN")
    
    return path