## Solution-1

- We are creating a hashlist where index represent alphabet position
  - hashlist [0,0,0,0...]: len->26
  - index [0,1,2,3,4..25]
- for one string we are increasing the value at the index of character by
  1 by iterating over it
- for second string we are decreasing the value by 1
- if the string are anagrams that have exact same letters then after both
  iteration hashlist have 0 value at all indices
- t(n)= O(n)
- s(n)=O(1)

## Solution-2

- Here we use Counter: which creates a frequency dictionary where keys are character and values no. of times the character occurs in string
- if both have same frequency dictionary then it is Anagram
