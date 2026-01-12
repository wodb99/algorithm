def solution(numbers, k):
    answer = 0
    cnt = 1
    idx = 0
    
    while True:
        if cnt == k:
            answer = numbers[idx]
            break
        idx = (idx + 2) % len(numbers)
        cnt += 1
            
    return answer