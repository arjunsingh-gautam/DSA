from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap=defaultdict(int)
        balloon="balloon"
        for ch in text:
            hashmap[ch]+=1
        if any(c not in hashmap for c in balloon):
            return 0
        else:
            return min(hashmap['b'],hashmap['a'],hashmap['l']//2,hashmap['o']//2,hashmap['n'])

        