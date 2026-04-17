# **<span style="color:#ff6b6b">Problem: Maximum Number of “balloon” Instances</span>**

You are given a string `text`.
Return the **maximum number of times the word `"balloon"` can be formed** using the characters from `text`.

Rules:

- Each character can be used **only once**.
- `"balloon"` requires specific character counts.

Required characters:

```text
b → 1
a → 1
l → 2
o → 2
n → 1
```

Example:

```text
text = "loonbalxballpoon"
```

Output:

```text
2
```

Because `"balloon"` can be formed **two times**.

---

# **<span style="color:#4ecdc4">Your Solution</span>**

```python
from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap=defaultdict(int)
        balloon="balloon"

        for ch in text:
            hashmap[ch]+=1

        if any(c not in hashmap for c in balloon):
            return 0
        else:
            return min(hashmap['b'],hashmap['a'],hashmap['l']//2,hashmap['o']//2,hashmap['n'])
```

Your logic:

```text
1. Count frequency of characters
2. Check if required characters exist
3. Compute limiting frequency
```

This is a **correct and efficient solution**.

---

# **<span style="color:#ffd166">Approach Used</span>**

You use the **Character Frequency Limitation Pattern**.

Idea:

```text
Each word "balloon" consumes certain characters.
The rarest required character determines how many words can be formed.
```

So we compute:

```text
min(available_characters / required_characters)
```

---

# **<span style="color:#a29bfe">Step-by-Step Explanation</span>**

### **Step 1: Count Character Frequencies**

```python
for ch in text:
    hashmap[ch]+=1
```

Example:

```text
text = "loonbalxballpoon"
```

Frequency map:

```text
{
b:2
a:2
l:4
o:4
n:2
...
}
```

---

### **Step 2: Check Required Characters Exist**

```python
any(c not in hashmap for c in balloon)
```

This checks whether any required letter is missing.

Example:

If `"b"` is missing:

```text
"balloon" cannot be formed
```

Return:

```text
0
```

---

### **Step 3: Compute Maximum Possible Words**

Each `"balloon"` requires:

```text
b → 1
a → 1
l → 2
o → 2
n → 1
```

So we divide counts:

```text
l_count // 2
o_count // 2
```

Then the smallest value determines the maximum number of `"balloon"` words.

Example:

```text
b=2
a=2
l=4
o=4
n=2
```

Possible balloons:

```text
min(2,2,4//2,4//2,2)
= min(2,2,2,2,2)
= 2
```

---

# **<span style="color:#00d2d3">Pseudocode</span>**

```
create frequency hashmap

for each character in text
    increase frequency

if any required character missing
    return 0

return minimum(
    count(b),
    count(a),
    count(l) // 2,
    count(o) // 2,
    count(n)
)
```

---

# **<span style="color:#feca57">Concept Used</span>**

This problem uses the **Frequency Limiting Principle**.

Key idea:

```text
The maximum number of words you can build
is limited by the scarcest required character.
```

Example:

```text
b=10
a=10
l=3
o=10
n=10
```

Since `"l"` is needed twice:

```text
3 // 2 = 1
```

So maximum `"balloon"` = **1**.

---

# **<span style="color:#ff9f43">Time Complexity</span>**

Let:

```text
n = len(text)
```

Building hashmap:

```text
O(n)
```

Checking characters:

```text
O(1)
```

Total:

```text
O(n)
```

---

# **<span style="color:#48dbfb">Space Complexity</span>**

Hashmap stores characters.

Maximum unique characters:

```text
26 letters
```

So:

```text
O(1)
```

constant space.

---

# **<span style="color:#1dd1a1">Rating Your Approach</span>**

| Category              | Rating     |
| --------------------- | ---------- |
| Correctness           | ⭐⭐⭐⭐⭐ |
| Optimality            | ⭐⭐⭐⭐⭐ |
| Pattern understanding | ⭐⭐⭐⭐⭐ |
| Code clarity          | ⭐⭐⭐⭐   |

Overall:

```text
9 / 10
```

Very good solution.

---

# **<span style="color:#ff6b6b">Small Optimization</span>**

The check:

```python
any(c not in hashmap for c in balloon)
```

is actually unnecessary.

Because:

```text
defaultdict returns 0 for missing keys
```

So we can directly compute:

```python
return min(
    hashmap['b'],
    hashmap['a'],
    hashmap['l']//2,
    hashmap['o']//2,
    hashmap['n']
)
```

---

# **<span style="color:#a29bfe">Cleaner Version</span>**

```python
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count = Counter(text)

        return min(
            count['b'],
            count['a'],
            count['l']//2,
            count['o']//2,
            count['n']
        )
```

---

# **<span style="color:#00d2d3">Pattern Used</span>**

This problem uses the **Character Resource Consumption Pattern**.

Structure:

```text
1. Count available resources
2. Determine resource requirements
3. Limiting resource determines output
```

---

# **<span style="color:#f368e0">Similar LeetCode Problems</span>**

Problems using **frequency limitation idea**:

1. Ransom Note
2. Jewels and Stones
3. Valid Anagram
4. Find All Anagrams in a String
5. Maximum Number of Words Formed

---

# **<span style="color:#ff6b6b">Key Insight</span>**

Whenever a problem asks:

```text
How many times can we build X from characters?
```

Think:

```text
frequency counting + limiting resource
```

Formula:

```text
min(available_characters / required_characters)
```

---

If you want, I can also show you **a general template for solving all frequency-based string problems (used in ~40+ LeetCode questions)**.
