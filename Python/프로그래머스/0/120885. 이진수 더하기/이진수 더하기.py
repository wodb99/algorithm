def solution(bin1, bin2):
    answer = ''
    a = bin1[::-1]
    b = bin2[::-1]
    
    temp1 = 1
    val1 = 0
    for i in a:
        val1 += temp1 * int(i)
        temp1 *= 2
    
    temp2 = 1
    val2 = 0
    for j in b:
        val2 += temp2 * int(j)
        temp2 *= 2
        
    res = val1 + val2
    return bin(res)[2:]