def solution(my_string):
    answer = ''
    temp = list(my_string.lower())
    temp.sort()
    for i in temp:
        answer += i
    return answer