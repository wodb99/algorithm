def solution(numbers):
    answer = 0
    temp = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for i in temp.keys():
        numbers = numbers.replace(i, temp[i])
        
    return int(numbers)