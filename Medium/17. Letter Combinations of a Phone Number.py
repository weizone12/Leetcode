def letterCombinations(digits: str):
    res = []
    numbers = {'2':'abc',
               '3':'def',
               '4':'ghi',
               '5':'jkl', 
               '6':'mno',
               '7':'pqrs',
               '8':'tuv',
               '9':'wxyz'}
    
    def addchar(i, s):
        if len(s) == len(digits):
            res.append(s)
            return
        for c in numbers[digits[i]]:
            addchar(i+1, s+c)
    
    if digits:
        addchar(0, "")
    return res