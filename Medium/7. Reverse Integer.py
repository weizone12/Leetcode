def reverse(x: int):
    max_num = 2**31-1
    min_num = -2**31
    strx = str(x)
    negative = 1
    res = 0
    if '-' in strx:
        negative = -1
        strx = strx.replace('-', "")
    res = strx[::-1]
    res = int(res) * negative
    if res < min_num or res > max_num:
        return 0
    return res