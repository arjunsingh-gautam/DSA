# Optimise 2 Pointer
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        largest=0
        while left<right:
            l=right-left
            h=min(heights[left],heights[right])
            if l*h>largest:
                largest=l*h
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return largest

# T(n)=O(n)
# S(n)=O(1)