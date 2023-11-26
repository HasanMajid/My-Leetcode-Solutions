def twoSum(nums: list[int], target: int) -> list[int]:
        for x in range(len(nums)):
            for y in range(len(nums)):
                if (nums[x] + nums[y] == target and x != y):
                    return [x,y]
                
