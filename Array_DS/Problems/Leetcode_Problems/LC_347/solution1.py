from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        result=set()
        for j in nums:
            freq[j]+=1
        for i in range(k):
            v1=sorted(freq.values(),reverse=True)[i]
            for l,v in freq.items():
                if v==v1:
                    result.add(l)

        return list(result)