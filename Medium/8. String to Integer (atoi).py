def myAtoi(s: str):
        max_num = 2**31-1
        min_num = -2**31
        i = 0
        res = 0
        negative = 1
        # check space
        while i < len(s) and s[i] == ' ':
            i += 1
        # check +/-
        if i < len(s) and s[i] == '+':
            i += 1
        elif i < len(s) and s[i] == '-':
            i += 1
            negative = -1
        # check number
        charset = set("0123456789")
        while i < len(s) and s[i] in charset:
            res = res * 10 + int(s[i])
            i += 1
        # check max/min num
        res *= negative
        if res < 0:
            return max(res, min_num)
        return min(res, max_num)