# Brute Force checking every pair
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        largest=0
        current=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                current=(j-i)*min(heights[i],heights[j])
                largest=max(current,largest)
        return largest        

# T(n)=O(n*n)
# S(n)=O(1)