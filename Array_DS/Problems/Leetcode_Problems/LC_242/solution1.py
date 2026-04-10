class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping=[0]*26
        for ch in s:
            index=ord(ch)-97
            mapping[index]+=1
        
        for ch in t:
            index=ord(ch)-97
            mapping[index]-=1

        if all([m==0 for m in mapping]):
            return True
        else:
            return False
        