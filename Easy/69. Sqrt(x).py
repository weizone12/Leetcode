def mySqrt(x: int):
    res = 1
    while res*res <= x:
        if res*res == x:
            return res
        res += 1
    return res-1