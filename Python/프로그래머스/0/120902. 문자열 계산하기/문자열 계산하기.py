def solution(my_string):
    answer = 0
    temp = list(my_string.split())
    for i in range(len(temp)):
        if temp[i - 1] == '+':
            answer += int(temp[i])
        elif temp[i - 1] == '-':
            answer -= int(temp[i])
        elif i == 0:
            answer += int(temp[i])
    return answer