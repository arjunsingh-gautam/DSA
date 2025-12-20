# Question:Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Eg.Input: nums = [1, 2, 3, 3] Output: true
# Eg. Input: nums = [1, 2, 3, 4] Output: false




# solution-1:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)>len(set(nums)):
            return True
        else: 
            return False
# Time Complexity: O(n) converting list to set
# space complexity: set store n elements: O(n)

# Solution-2: Using hashset
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for i in nums:
            if i in set:
                return True
            hashset.add(i)
        return False
# Time Complexity:O(n): n iterations
# Space Complexity: O(n): set stores n elements

# solution-3: Sorting:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(num)):
            if nums[i]==nums[i-1]:
                return True
        return False

# Time complexity: O(nlogn)
# Space Complexity: O(1) in place sorting

