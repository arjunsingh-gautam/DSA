class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            p1=numbers[i]
            for j in range(i+1,len(numbers)):
                p2=numbers[j]
                if (p1+p2==target):
                    return [i+1,j+1]

# Brute Force
# T(n)=O(n*n)
# Two pointers
