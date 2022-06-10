def strStr(haystack: str, needle: str):
    if needle in haystack:
        return haystack.index(needle)
    return -1