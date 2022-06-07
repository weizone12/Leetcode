def runningSum(nums: list[int]):
    res = []
    add, i = 0, 0
    while i < len(nums):
        res.append(nums[i]+add)
        add += nums[i]
        i += 1
    return res