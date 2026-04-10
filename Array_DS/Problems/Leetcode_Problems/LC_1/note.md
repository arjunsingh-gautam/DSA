## Solution-1 (Brute Force)

- adding each possible pair and checking against target
- when matched return pair
- Eg. [1,2,5] target=7
  (1,2) (1,5) (2,5)
- t(n):O(n^2)

## Solution-2(Optimised): Pattern -> Hashmap

- hasmap={} key=element in nums, value:index of element
- Traversing the the nums list:
  - if (target-nums[i]) not in hashmap --> add it to hashmap
  - if present return the value i.e index + index of current iteration
