def solution(my_string):
    answer = ''
    temp = list(my_string)
    for i in temp:
        if i.islower():
            answer += i.upper()
        else:
            answer += i.lower()
    return answer