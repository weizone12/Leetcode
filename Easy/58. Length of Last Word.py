def lengthOfLastWord(s: str):
    i, res = len(s)-1, 0
    while s[i] == ' ':
        i -= 1
    while s[i] != ' ' and i >= 0:
        res += 1
        i -= 1
    return res