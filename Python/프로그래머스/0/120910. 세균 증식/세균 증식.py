def solution(n, t):
    count = 0
    while True:
        n *= 2
        count += 1
        if count == t:
            break
    return n