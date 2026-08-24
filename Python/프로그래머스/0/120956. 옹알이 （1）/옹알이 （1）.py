def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        temp = b
        
        for w in words:
            temp = temp.replace(w, " ")
            
        if temp.strip() == "":
            answer += 1
            
    return answer