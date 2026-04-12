# **<span style="color:#ff6b6b">Problem: Group Anagrams</span>**

Given a list of strings `strs`, group all **anagrams** together.

Two strings are **anagrams** if they contain the **same characters with the same frequencies**, possibly in a different order.

Example:

```
Input:
["eat","tea","tan","ate","nat","bat"]

Output:
[["eat","tea","ate"],["tan","nat"],["bat"]]
```

---

# **<span style="color:#4ecdc4">Your Provided Solution</span>**

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for s in strs:
            mapping = [0] * 26
            for ch in s:
                index = ord(ch) - ord('a')
                mapping[index] += 1
            key = tuple(mapping)
            anagram_dict[key].append(s)

        return list(anagram_dict.values())
```

Your approach uses:

```
Frequency List + HashMap
```

This is **one of the optimal and interview-preferred approaches**.

---

# **<span style="color:#ffd166">Approach Used in Your Solution</span>**

Your approach works in **three stages**:

### **1️⃣ Character Frequency Representation**

For every string:

```
create frequency list of size 26
```

Example:

```
eat
```

frequency:

```
a=1
e=1
t=1
```

frequency array:

```
[1,0,0,0,1,0,0,...,1]
```

---

### **2️⃣ Convert Frequency List → Hashable Key**

Lists cannot be used as dictionary keys.

So you convert:

```
list → tuple
```

Example:

```
(1,0,0,0,1,0,...,1)
```

This tuple uniquely represents an anagram group.

---

### **3️⃣ Store Strings in HashMap**

Structure:

```
key   -> list of anagrams
```

Example:

```
(1,0,0,0,1,0,...,1) → ["eat","tea","ate"]
```

---

# **<span style="color:#a29bfe">Pseudocode</span>**

```
function groupAnagrams(strs):

    create hashmap anagram_dict

    for each string s in strs:

        create frequency array of size 26 filled with 0

        for each character ch in s:
            index = ascii(ch) - ascii('a')
            increment frequency[index]

        convert frequency array to tuple

        append string to hashmap[tuple]

    return values of hashmap
```

---

# **<span style="color:#00d2d3">Concept Used</span>**

## **Character Frequency Encoding**

Core idea:

```
Two strings are anagrams
⇓
They have identical character counts
```

Instead of sorting:

```
eat → aet
tea → aet
```

You use:

```
character frequency vector
```

Example:

```
eat → [1,0,0,0,1,0,...,1]
tea → same vector
ate → same vector
```

Thus:

```
same frequency → same group
```

---

# **<span style="color:#feca57">Pattern Used</span>**

### **Hashing + Canonical Representation Pattern**

Steps:

```
1. Convert data into canonical form
2. Use canonical form as hashmap key
3. Group elements with same representation
```

Canonical representations can be:

```
sorted string
frequency array
bitmask
```

Your canonical form:

```
character frequency tuple
```

---

# **<span style="color:#ff9f43">Step-by-Step Example</span>**

Input:

```
["eat","tea","tan","ate","nat","bat"]
```

Processing:

```
eat → (1,0,0,0,1,0,...,1)
tea → same key
ate → same key
```

HashMap:

```
(1,0,0,0,1...) → ["eat","tea","ate"]
```

Next:

```
tan → (1,0,0,0,0,0,...)
nat → same key
```

HashMap:

```
key → ["tan","nat"]
```

---

# **<span style="color:#48dbfb">Time Complexity Analysis</span>**

Let:

```
n = number of strings
k = average length of string
```

### **Frequency Construction**

For each string:

```
O(k)
```

For all strings:

```
O(n × k)
```

Dictionary operations:

```
O(1)
```

### **Final Time Complexity**

```
O(n × k)
```

This is **optimal**.

---

# **<span style="color:#1dd1a1">Space Complexity Analysis</span>**

Dictionary stores:

```
n strings
```

Frequency array size:

```
26
```

Total:

```
O(n × k)
```

Auxiliary structure:

```
26 → constant
```

So extra space:

```
O(n)
```

---

# **<span style="color:#ff6b6b">Rating Your Approach</span>**

| Category            | Rating     |
| ------------------- | ---------- |
| Correctness         | ⭐⭐⭐⭐⭐ |
| Optimality          | ⭐⭐⭐⭐⭐ |
| Pattern recognition | ⭐⭐⭐⭐⭐ |
| Code clarity        | ⭐⭐⭐⭐⭐ |

### **Overall**

```
9.5 / 10
```

This is the **best practical solution used in interviews**.

---

# **<span style="color:#54a0ff">Other Approaches</span>**

## **Approach 1 — Sorting Key**

Idea:

```
sort characters
```

Example:

```
eat → aet
tea → aet
ate → aet
```

Code concept:

```
key = "".join(sorted(word))
```

### Complexity

```
Sorting = O(k log k)
Total = O(n × k log k)
```

Slower than frequency approach.

---

## **Approach 2 — Prime Number Hashing (Advanced)**

Assign prime numbers to characters.

Example:

```
a → 2
b → 3
c → 5
```

Compute product.

```
eat → 2 × 11 × 71
tea → same
```

Problems:

```
overflow risk
large integers
```

Rarely used.

---

# **<span style="color:#f368e0">LeetCode Problems With Similar Pattern</span>**

These problems use **frequency hashing or canonical grouping**.

### **Anagram / Frequency Pattern**

1. **Valid Anagram**

2. **Find All Anagrams in a String**

3. **Group Anagrams**

4. **Permutation in String**

5. **Minimum Window Substring**

6. **Ransom Note**

7. **Determine if Two Strings Are Close**

---

# **<span style="color:#00d2d3">Practice Questions With Similar Pattern</span>**

### **Question 1**

Group words that have the **same character frequency**.

---

### **Question 2**

Find all substrings of `s` that are anagrams of `p`.

---

### **Question 3**

Check if two strings are **permutations of each other**.

---

### **Question 4**

Given list of words, group words that can be **rearranged to match**.

---

### **Question 5**

Find number of **anagram pairs** in a list.

---

# **<span style="color:#a29bfe">Key Pattern Recognition Tip</span>**

Whenever you see problems involving:

```
anagram
permutation
rearrangement of characters
character equality ignoring order
```

Think immediately:

```
1️⃣ Sorting
2️⃣ Frequency array
3️⃣ Hashmap grouping
```

This pattern appears in **many sliding window and hashing problems**.

---

If you want, I can also show you something extremely useful for interviews:

**The 12 core HashMap patterns that solve ~40% of DSA interview questions.**
