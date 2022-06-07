def isMatch(s: str, p: str):
    si, pi = 0, 0
    while si < len(s) and pi < len(p):
        if p[pi] == '.':
            pi += 1
            si += 1
        elif p[pi] == '*':
            if pi == len(p)-1:
                return True
            else:
                pi += 1
                if p[pi] not in s[si:len(s)]: 
                    return False
            si += len(s[si:s.index(p[pi])+1])
        elif s[si] == p[pi]:
            pi += 1
            si += 1
        else:
            return False
    if si == len(s)-1 and pi == len(p)-1:
        return True
    return False