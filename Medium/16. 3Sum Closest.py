def threeSumClosest(nums: list[int], target: int):
    res = nums[0]+nums[1]+nums[2]
    nums.sort()
    for i, val in enumerate(nums):
        l, r = i+1, len(nums)-1
        while l < r:
            add = val + nums[l] + nums[r]
            
            if add < target:
                l += 1
            elif add > target:
                r -= 1
            else:
                return target
            
            if abs(add-target) < abs(res-target):
                res = add   
    return res