def longestCommonPrefix(strs: list[str]):
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += s[i]
    return res