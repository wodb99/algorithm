def solution(num_list):
    last = num_list[-1]
    second = num_list[-2]
    if last > second:
        temp = last - second
    else:
        temp = last * 2
    num_list.append(temp)
    return num_list