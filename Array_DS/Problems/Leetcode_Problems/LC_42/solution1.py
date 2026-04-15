class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxL=0
        maxR=0
        L=[0]*n
        R=[0]*n
        water=0
        for i in range(n):
            current=height[i]
            L[i]=maxL
            maxL=max(current,maxL)

        for j in range(n-1,-1,-1):
            current=height[j]
            R[j]=maxR
            maxR=max(current,maxR)

        for i in range(n):
            potential=min(L[i],R[i])
            if (potential-height[i]<=0):
                continue
            else:
                water+=(potential-height[i])

        return water
        