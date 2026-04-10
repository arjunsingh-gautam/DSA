# Approach:

- Hume duplicate agar nums list mai duplicate hai toh true return nahi hai to false
- For this we can set since set data-structure remove duplicate
- We can typecast list into set it automatically removes from the list
- space complexity:O(n)
- time complexity: O(n) : due to scanning of the list

# Brute Force Approach:

- checking every pair
- [1,2,3,3] here we check pairs using nested loops:
  (1,2),(1,3),(1,3)
  (2,3) (2,3)
  (3,3) : duplicates return: True
- Time complexity:O(n^2)
- Space complexity:O(1)

# Approach-4

- Sorting the list and then using two moving pointer and check if adjacent pairs are equal
- if equal: return True
- else after complete looping : False
