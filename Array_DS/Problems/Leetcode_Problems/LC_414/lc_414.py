# Problem Statement:
""" Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1. """

# Solution:
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        else:
            if len(set(nums))==len(nums):
                return(sorted(nums)[len(nums)-3])
            elif len(set(nums))<len(nums):
                new_nums=set(nums)
                if len(new_nums)>2:
                    return(sorted(new_nums)[len(new_nums)-3])
                else:
                    return max(set(nums))
        
# Optimised Solution t(n)=O(n) and s(n)=O(1)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = None

        for x in nums:
            # Step 1: skip duplicates
            if x == max1 or x == max2 or x == max3:
                continue

            # Step 2: new maximum
            if max1 is None or x > max1:
                max3 = max2
                max2 = max1
                max1 = x

            # Step 3: new second maximum
            elif max2 is None or x > max2:
                max3 = max2
                max2 = x

            # Step 4: new third maximum
            elif max3 is None or x > max3:
                max3 = x

        # Step 5: result
        return max3 if max3 is not None else max1
