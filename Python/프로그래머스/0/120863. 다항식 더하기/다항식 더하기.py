def solution(polynomial):
    x_coef = 0
    constant = 0
    
    # 항 단위로 분리
    terms = polynomial.split('+')
    
    # 각 항 처리
    for term in terms:
        term = term.strip()
        
        # 숫자만 있으면 상수
        if term.isdigit():
            constant += int(term)
            
        # x가 포함된 항
        else:
            if term == 'x':
                x_coef += 1
            else:
                x_coef += int(term[:-1])
    
    # 결과 문자열 생성
    if x_coef == 0:
        return str(constant)

    if x_coef == 1:
        x_part = 'x'
    else:
        x_part = f'{x_coef}x'
    
    if constant == 0:
        return x_part
    
    return f'{x_part} + {constant}'