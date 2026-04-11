class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        mapping=[0]*len(nums)
        for i in nums:
            index=i-1
            mapping[index]+=1
        for j in range(len(nums)):
            if mapping[j]==0:
                result.append(j+1)
        return result
    
# T(n):O(n)
# S(n):O(n)