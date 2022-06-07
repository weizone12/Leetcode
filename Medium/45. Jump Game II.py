def jump(nums: list[int]):
    res = 0
    left = right = 0
    while right < len(nums):
        faridx = 0
        for i in range(left, right+1):
            faridx = max(faridx, i+nums[i])
        left = right + 1
        right = faridx
        res += 1
    return res