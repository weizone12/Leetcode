def lengthOfLongestSubstring(s: str):
    charset = set()
    length = 0
    re_num = 0
    for i in range(len(s)):
        while s[i] in charset:
            charset.remove(s[re_num])
            re_num += 1
        charset.add(s[i])
        length = max(length, i+1-re_num)
    return length