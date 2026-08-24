def solution(my_string):
    answer = []
    temp = list(my_string)
    for i in temp:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()
    return answer