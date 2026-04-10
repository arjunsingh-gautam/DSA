# **<span style="color:#7aa2f7">Problem Analysis – Group Anagrams</span>**

We analyze the following solution step-by-step to determine:

1. **Time Complexity**
2. **Space Complexity**
3. **Pattern Used**
4. **Concepts Used**

```python
from typing import List
from collections import defaultdict

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

---

# **<span style="color:#9ece6a">1. Key Idea of the Algorithm</span>**

Two strings are **anagrams** if they contain the **same characters with the same frequency**.

Example:

```
eat
tea
ate
```

All have identical frequency counts:

```
a → 1
e → 1
t → 1
```

The algorithm:

1. **Compute a character frequency vector**
2. **Use it as a hash key**
3. **Group strings with identical vectors**

Example mapping:

```
"eat" → (1,0,0,...,1,...,1,...)
"tea" → (1,0,0,...,1,...,1,...)
```

Both map to the **same key**, so they belong in the same group.

---

# **<span style="color:#9ece6a">2. Step-by-Step Execution</span>**

Assume:

```
strs = ["eat","tea","tan","ate","nat","bat"]
```

### **Step 1 – Initialize Hash Map**

```python
anagram_dict = defaultdict(list)
```

Structure:

```
{
   key(tuple): [list_of_anagrams]
}
```

Time:

```
O(1)
```

Space:

```
O(1)
```

---

### **Step 2 – Iterate Through All Strings**

```python
for s in strs:
```

If:

```
n = number of strings
```

Then loop runs:

```
n times
```

Time:

```
O(n)
```

---

### **Step 3 – Create Character Frequency Array**

```python
mapping = [0] * 26
```

Creates array:

```
[0,0,0,...,0]
```

Length = 26 because lowercase English alphabet.

Time:

```
O(26) ≈ O(1)
```

Space:

```
O(26) ≈ O(1)
```

---

### **Step 4 – Count Character Frequencies**

```python
for ch in s:
```

Let:

```
k = length of string
```

This loop runs:

```
k times
```

Operations inside:

```python
index = ord(ch) - ord('a')
mapping[index] += 1
```

Both are constant time.

Time per string:

```
O(k)
```

---

### **Step 5 – Convert List to Tuple**

```python
key = tuple(mapping)
```

Reason: lists cannot be dictionary keys.

Tuple creation cost:

```
O(26)
```

Which simplifies to:

```
O(1)
```

---

### **Step 6 – Insert Into Hash Table**

```python
anagram_dict[key].append(s)
```

Hash table insertion:

```
Average case → O(1)
```

---

### **Step 7 – Convert Values to List**

```python
return list(anagram_dict.values())
```

If number of groups = `g`.

Cost:

```
O(g)
```

Worst case:

```
g = n
```

So:

```
O(n)
```

---

# **<span style="color:#e0af68">3. Total Time Complexity</span>**

Let:

```
n = number of strings
k = average length of string
```

Main work occurs here:

```
for s in strs:
    for ch in s:
```

Cost:

```
O(n * k)
```

Other operations are constant.

### **Final Time Complexity**

```
O(n * k)
```

Where:

- `n` = number of strings
- `k` = average string length

---

# **<span style="color:#e0af68">4. Space Complexity</span>**

We analyze all memory used.

---

### **Dictionary Storage**

Worst case:

```
each string is unique
```

Dictionary entries:

```
n keys
```

Each key:

```
tuple of size 26
```

Space:

```
O(26n)
```

Which simplifies to:

```
O(n)
```

---

### **Output Storage**

All strings stored in result groups.

Space:

```
O(n * k)
```

because we store all strings.

---

### **Frequency Array**

```
mapping = [0]*26
```

Temporary.

Space:

```
O(1)
```

---

### **Final Space Complexity**

Dominant term:

```
O(n * k)
```

---

# **<span style="color:#bb9af7">5. Pattern Used in This Problem</span>**

### **Hashing Pattern**

Core idea:

```
Generate canonical representation
→ Use it as hash key
→ Group elements
```

Pattern structure:

```
key = representation(item)
hashmap[key].append(item)
```

Applications of this pattern:

- Group Anagrams
- Frequency based grouping
- Duplicate detection
- Bucket grouping

---

# **<span style="color:#bb9af7">6. Concepts Used</span>**

### **1. Hash Tables**

Dictionary used for grouping:

```
key → list of anagrams
```

Average access time:

```
O(1)
```

---

### **2. Character Frequency Encoding**

Each string converted to a **frequency vector**:

```
[ count(a), count(b), ..., count(z) ]
```

This uniquely identifies an anagram group.

---

### **3. Tuple Hashing**

Python dictionaries require **immutable keys**.

So:

```
list → tuple
```

---

### **4. ASCII Arithmetic**

Character index computed using:

```python
ord(ch) - ord('a')
```

Example:

```
ord('c') = 99
ord('a') = 97

index = 2
```

---

### **5. defaultdict**

Simplifies dictionary operations:

Instead of:

```python
if key not in dict:
    dict[key] = []
```

`defaultdict(list)` automatically initializes.

---

# **<span style="color:#7aa2f7">Final Complexity Summary</span>**

| Metric           | Complexity                       |
| ---------------- | -------------------------------- |
| Time Complexity  | **O(n × k)**                     |
| Space Complexity | **O(n × k)**                     |
| Pattern          | **Hashing + Frequency Encoding** |
| Data Structure   | **Hash Map (Dictionary)**        |

Where:

```
n = number of strings
k = average string length
```

---

If you want, I can also explain something **important for interviews**:

- **Why this solution is faster than sorting based solution**
- **When to choose frequency vector vs sorted string**
- **How interviewers expect you to derive this solution step-by-step**.
