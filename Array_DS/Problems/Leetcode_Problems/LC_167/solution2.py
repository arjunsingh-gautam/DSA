class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(numbers)):
            hashmap[numbers[i]]=i
        for i in range(len(numbers)):
            if (target-numbers[i] in hashmap): #O(1) lookup
                return [i+1,hashmap.get(target-numbers[i])+1]

# Optimised using hashmap:
# T(n)=O(n)
# S(n)=O(n)
        
