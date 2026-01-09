def solution(numbers):
    max = float('-inf')
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            res = numbers[i] * numbers[j]
            if res > max:
                max = res
    return max