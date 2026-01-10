def solution(my_string):
    answer = 0
    num = ''
    for i in my_string:
        if i.isdigit():
            num += i
        else:
            if num:
                answer += int(num)
                num = ''
                
    if num: # 맨 끝이 숫자라면 다음에 올 문자가 없기 때문에 더하지 않고 건너뛰게 됨
        answer += int(num)
        
    return answer