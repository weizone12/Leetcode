def removeElement(nums: list[int], val: int):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.remove(nums[i])
        else:
            i += 1
    return len(nums)