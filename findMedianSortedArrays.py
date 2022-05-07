
import time

def findMedianSortedArrays(nums1, nums2) -> float:
    nums = nums1 + nums2
    length = len(nums)
    nums.sort()
        
    if (length % 2 == 1):
        return nums[int((length-1)/2) ]
    else:
        return (nums[int(((length) / 2) - 1)] + nums[int(((length) / 2) )]) / 2 
    
## This one only works for lists that are in descending order and increment by 1 (e.g. [1,2,3,4])
def findMedianSortedArrays2(nums1, nums2) -> float:
    nums = nums1 + nums2
    length = len(nums)
    result = 0
    for x in nums:
        result += x
    result /= length
    return result

## This one tries to be efficient, sometimes its faster, sometimes not; depends on the input
def findMedianSortedArrays3(nums1, nums2) -> float:
    lis = sorted(nums1 + nums2)
    length = len(lis)
    sumting = sum(lis) 
    if sumting / 2 == lis[-1]:
        return (sumting/length)
    if (length % 2 == 1):
        return lis[length // 2]
    else:
        return (lis[(length // 2) - 1] + lis[length // 2 ]) / 2 

def findMedianSortedArrays4(nums1, nums2) -> float:
    lis = sorted(nums1 + nums2)
    length = len(lis)
    sumting = lis[0]

    for x in range(1,length+1):
        if (x == length):
            return sumting / length
        elif lis[x] == lis[x-1]:
            sumting += lis[x]
        else:
            break
                 
    if (length % 2 == 1):
        return lis[length // 2]
    else:
        return (lis[(length // 2) - 1] + lis[length // 2 ]) / 2 

start_time = time.time()
print(findMedianSortedArrays4([1,3],[4,2]))
print("--- %s seconds ---" % (time.time() - start_time))
        