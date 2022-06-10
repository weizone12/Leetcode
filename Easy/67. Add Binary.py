def addBinary(a: str, b: str):
    a = a[::-1]
    b = b[::-1]
    i, carry = 0, 0
    res = ""
    
    while len(a) < len(b):
        a += '0'
    while len(a) > len(b):
        b += '0'
    
    while i < len(a):
        add = int(a[i]) + int(b[i]) + carry
        carry = 0
        if add >= 2:
            res += str(add-2)
            carry += 1
        else:
            res += str(add)
        i += 1
    
    if carry:
        res += str(carry)
    
    return res[::-1]
