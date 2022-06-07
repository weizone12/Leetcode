def findMedianSortedArrays(nums1: list[int], nums2: list[int]):
    num = nums1 + nums2
    num.sort()
    if len(num) % 2 == 0:
        return float("%.5f"%((num[len(num)//2-1] + num[len(num)//2])/2))
    else:
        return float("%.5f"%(num[len(num)//2]))