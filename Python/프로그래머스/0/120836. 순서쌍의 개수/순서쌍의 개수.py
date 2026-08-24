def solution(n):
    answer = 0
    res = set()
    for i in range(1, n+1):
        if n % i == 0:
            res.add(i)
    res = list(res)
    answer = len(res)
    return answer