def solution(n):
    answer = 0
    i = 0
    while True:
        i += 1
        temp = i ** 2
        if temp == n:
            answer = 1
            break
        if n < temp:
            answer = 2
            break
    return answer