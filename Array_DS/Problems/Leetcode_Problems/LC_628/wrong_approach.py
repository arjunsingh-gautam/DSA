class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        product=nums[0]*nums[1]*nums[2]
        best=0
        previous=[nums[i] for i in range(3)]
        if len(nums)==3:
            return reduce(lambda a,b:a*b,nums)
        else:
            for i in range(3,len(nums)):
                current=nums[i]
                for j in range(len(previous)):
                    best=max(int((product*current)/previous[j]),best)
                product=best
                previous.append(current)
            return best
        