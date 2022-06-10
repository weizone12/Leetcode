def removeDuplicates(nums: list[int]):
    intset = set()
    i = 0
    while i < len(nums):
        if nums[i] in intset:
            nums.remove(nums[i])
        else:
            intset.add(nums[i])
            i += 1
    return len(nums)