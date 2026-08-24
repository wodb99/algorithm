def solution(my_string, num1, num2):
    answer = ''
    temp = list(my_string)
    temp[num1], temp[num2] = temp[num2], temp[num1]
    for i in temp:
        answer += i
    return answer