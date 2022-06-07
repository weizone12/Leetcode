def maxArea(height: list[int]):
    l, r = 0, len(height)-1
    area = 0
    while l != r:
        min_num = min(height[l], height[r])
        if area < min_num * (r-l):
            area = min_num * (r-l)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return area