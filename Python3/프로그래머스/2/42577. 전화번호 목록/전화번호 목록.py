def solution(phone_book):
    phone_set = set(phone_book)

    for number in phone_book:
        temp = ""
        for ch in number:
            temp += ch
            
            if temp in phone_set and temp != number:
                return False

    return True