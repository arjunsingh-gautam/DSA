# **<span style="color:#ff6b6b">Problem: Jewels and Stones</span>**

You are given two strings:

- `jewels` → characters representing **types of jewels**
- `stones` → characters representing **stones you have**

Each character in `stones` is a stone you own.

Goal:

```text
Count how many stones are jewels.
```

Example:

```text
jewels = "aA"
stones = "aAAbbbb"

Output = 3
```

Explanation:

```text
stones → a A A b b b b
jewels → a A
```

So the jewels are:

```text
a A A → total = 3
```

---

# **<span style="color:#4ecdc4">Your Solution</span>**

```python
from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_total=0
        hashmap=defaultdict(int)

        for stone in stones:
            hashmap[stone]+=1

        for jewel in jewels:
            if jewel in hashmap:
                jewels_total+=hashmap.get(jewel)

        return jewels_total
```

Your idea:

```text
1. Count frequency of stones
2. Check which stones are jewels
3. Add their frequencies
```

This approach is **correct and efficient**.

---

# **<span style="color:#ffd166">Approach Used</span>**

Your algorithm works in **two phases**.

---

## **Phase 1: Count Stone Frequencies**

You create a **frequency hashmap**.

Structure:

```text
key   → stone character
value → number of times it appears
```

Example:

```text
stones = "aAAbbbb"
```

Hashmap becomes:

```text
{
'a':1
'A':2
'b':4
}
```

---

## **Phase 2: Count Jewels**

Now iterate through jewels.

```text
jewels = "aA"
```

Check:

```text
a → present → +1
A → present → +2
```

Total:

```text
3
```

---

# **<span style="color:#a29bfe">Pseudocode</span>**

```
create hashmap

for each stone in stones
    increase frequency

jewel_count = 0

for each jewel in jewels
    if jewel exists in hashmap
        jewel_count += hashmap[jewel]

return jewel_count
```

---

# **<span style="color:#00d2d3">Concept Used</span>**

This solution uses the **Frequency Counting Pattern**.

Idea:

```text
Instead of scanning the string repeatedly,
store counts in a hashmap.
```

Structure:

```text
character → frequency
```

This pattern appears in many string problems.

---

# **<span style="color:#feca57">Time Complexity</span>**

Let:

```text
n = len(stones)
m = len(jewels)
```

Building hashmap:

```text
O(n)
```

Checking jewels:

```text
O(m)
```

Total:

```text
O(n + m)
```

Which simplifies to:

```text
O(n)
```

---

# **<span style="color:#ff9f43">Space Complexity</span>**

Hashmap stores characters.

Worst case:

```text
O(k)
```

Where `k` = unique characters.

In practice:

```text
≤ 52 (A–Z, a–z)
```

So:

```text
O(1)
```

---

# **<span style="color:#1dd1a1">Rating Your Approach</span>**

| Category        | Rating     |
| --------------- | ---------- |
| Correctness     | ⭐⭐⭐⭐⭐ |
| Time complexity | ⭐⭐⭐⭐⭐ |
| Code clarity    | ⭐⭐⭐⭐   |
| Space usage     | ⭐⭐⭐⭐   |

Overall:

```text
9 / 10
```

Good solution.

---

# **<span style="color:#ff6b6b">Even Simpler Optimal Approach</span>**

We can solve this using a **set**.

Key idea:

```text
Check membership quickly.
```

Code:

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set=set(jewels)
        count=0

        for stone in stones:
            if stone in jewel_set:
                count+=1

        return count
```

---

### Complexity

Time:

```text
O(n)
```

Space:

```text
O(m)
```

This solution is **simpler and cleaner**.

---

# **<span style="color:#48dbfb">Why Set Is Better Here</span>**

You only need to know:

```text
Is this stone a jewel?
```

You **do not need frequencies**.

So set membership is enough.

---

# **<span style="color:#a29bfe">Pattern Used</span>**

This problem uses:

```text
Hash Set / Hash Map Membership Pattern
```

Used for:

```text
fast lookup problems
duplicate detection
membership queries
```

---

# **<span style="color:#00d2d3">Similar LeetCode Problems</span>**

Problems using **hashmap / set membership**:

1. Contains Duplicate
2. Valid Anagram
3. Intersection of Two Arrays
4. Longest Substring Without Repeating Characters
5. Ransom Note

---

# **<span style="color:#f368e0">Practice Questions With Same Pattern</span>**

Try problems where **membership lookup is key**.

Example questions:

### Question 1

Count characters in string that appear in another string.

---

### Question 2

Check if two arrays share at least one common element.

---

### Question 3

Find the first repeated character in a string.

---

### Question 4

Find number of unique characters in a string.

---

### Question 5

Check if a word can be constructed from characters of another word.

---

# **<span style="color:#ff6b6b">Key Insight</span>**

Whenever the problem asks:

```text
Does element X belong to set Y?
```

Think immediately:

```text
Use a HashSet
```

because membership lookup becomes:

```text
O(1)
```

---

If you want, I can also show you **the 6 most important HashMap patterns used in 70+ LeetCode problems**.
