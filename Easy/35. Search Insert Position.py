def searchInsert(nums: list[int], target: int):
    l, r = 0, len(nums)-1
    while l <= r:
        if nums[l] == target:
            return l
        if nums[l] < target:
            l += 1
        else:
            r -= 1
    return l