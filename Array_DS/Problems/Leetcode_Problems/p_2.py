# Question:
#link:https://leetcode.com/problems/valid-anagram/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# solution-1:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)

# Time complexity: O(nlogn + nlogn +n)=O(nlong)
# Space Complexity:O(n)


# solution-2: O(n) time complexity
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Time complexity:O(3n)==O(n)
# space complexity:O(k): k unique values in anagram