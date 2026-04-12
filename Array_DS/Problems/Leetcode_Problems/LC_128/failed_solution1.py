class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums=sorted(set(nums))
        length=0
        for i in range(len(sorted_nums)-1):
            current=sorted_nums[i]
            next=sorted_nums[i+1]
            if next==current+1:
                length+=1
                print(length)
            else:
                break
        return length

# Why failing:
"""
- Not able to handle edgecaase empty lisst
"""
