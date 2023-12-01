## This solution is O(N^2) and exceeds the time limit on Leetcode
def maxArea(height: list[int]) -> int:
    most = 0
    length = len(height)
    for x in range(length):
        for y in range(length):
            h = min(height[x], height[y])
            w = y - x
            amount = h * w
            if amount > most:
                most = amount
    return most

## O(N) solution
def maxArea2(height: list[int]) -> int:
    length = len(height)
    maxA = 0
    l = 0
    r = length - 1
    while r - l != 0:
        h = min(height[l], height[r])
        w = r - l
        amount = h * w
        if amount > maxA:
            maxA = amount
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxA
