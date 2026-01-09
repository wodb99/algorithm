def solution(numbers, direction):
    val = len(numbers)
    answer = [0] * val
    if direction == 'right':
        for i in range(val):
            idx = (i + val + 1) % val
            answer[idx] = numbers[i]
    else:
        for i in range(val):
            idx = (i + val - 1) % val
            answer[idx] = numbers[i]
    return answer