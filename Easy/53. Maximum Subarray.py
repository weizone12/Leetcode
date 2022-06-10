def maxSubArray(nums: list[int]):
    cur = 0
    maxSum = nums[0]
    for num in nums:
        if cur < 0:
            cur = 0
        cur += num
        maxSum = max(maxSum, cur)
    return maxSum