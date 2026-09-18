def solution(numbers):
    number_set = set()
    
    def dfs(current, remaining):
        if current:
            number_set.add(int(current))
            
        for i in range(len(remaining)):
            dfs(current + remaining[i], remaining[:i] + remaining[i+1:])
            
    def is_prime(n):
        if n < 2:
            return False
        
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
            
        return True
    
    dfs("", numbers)
    
    answer = 0
    for num in number_set:
        if is_prime(num):
            answer += 1
            
    return answer