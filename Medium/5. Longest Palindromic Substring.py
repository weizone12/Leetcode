def longestPalindrome(s: str):
    resLen = 0
    for idx in range(len(s)):
        left, right = idx, idx
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > resLen:
                res = s[left:right+1]
                resLen = right - left + 1
            left -= 1
            right += 1
        
        left, right = idx, idx + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > resLen:
                res = s[left:right+1]
                resLen = right - left + 1
            left += 1
            right += 1
    return res