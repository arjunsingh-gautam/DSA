from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_total=0
        hashmap=defaultdict(int)
        for stone in stones:
            hashmap[stone]+=1

        for jewel in jewels:
            if jewel in hashmap:
                jewels_total+=hashmap.get(jewel)

        return jewels_total
            
# T(n)=O(n)
# S(n)=O(1)
            