from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict=defaultdict(list)
        for s in strs:
            mapping=[0]*26
            for c in s:
                index=ord(c)-97
                mapping[index]+=1
            key=tuple(mapping)
            anagram_dict[key].append(s)

        return list(anagram_dict.values())
                

 # t(n)=O(n*k)
 # s(n)=O(n*k)          
       

   