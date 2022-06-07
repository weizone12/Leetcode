def twoSum(nums:list, target:int):
    dict1 = {}
    for idx, num in enumerate(nums):
        if num not in dict1:
            dict1[target-num] = idx
        else:
            return [dict1[num], idx]