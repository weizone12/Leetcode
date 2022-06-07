def convert(s: str, numRows: int):
    if numRows == 1: return s
    rows = ["" for i in range(numRows)]
    row, step = 0, 1
    for char in s:
        rows[row] += char
        if row == 0:
            step = 1
        elif row == numRows-1:
            step = -1
        row += step
    return "".join(rows)