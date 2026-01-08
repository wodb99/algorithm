def solution(n, k):
    temp = n // 10
    answer = 12000 * n + 2000 * k - 2000 * temp
    return answer