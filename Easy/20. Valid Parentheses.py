def isValid(s: str):
    tmp = []
    chardict = {')':'(', ']':'[', '}':'{'}
    for i in s:
        if i in chardict:
            if tmp and tmp[-1] == chardict[i]:
                tmp.pop()
            else:
                return False
        else:
            tmp.append(i)
    return False if tmp else True