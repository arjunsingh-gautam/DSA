from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap=defaultdict(int)
        for ch in magazine:
            hashmap[ch]+=1
        
        for ch in ransomNote:
            if ch not in hashmap:
                return False
            elif hashmap[ch]==1:
                del hashmap[ch]
            else:
                hashmap[ch]-=1
        return True

# T(n)=O(m+n)=O(n)
# S(n)=O(1)

        