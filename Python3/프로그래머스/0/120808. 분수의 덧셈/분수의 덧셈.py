import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    res_denom = lcm(denom1, denom2)
    res_numer = numer1 * (res_denom // denom1) + numer2 * (res_denom // denom2)
    
    g = math.gcd(res_numer, res_denom)
    
    answer.append(res_numer // g)
    answer.append(res_denom // g)
    
    return answer