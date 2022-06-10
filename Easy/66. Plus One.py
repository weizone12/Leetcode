def plusOne(digits: list[int]):
    digits = digits[::-1]
    i = 0
    while i < len(digits):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits[::-1]
        i += 1
    digits.append(1)
    return digits[::-1]