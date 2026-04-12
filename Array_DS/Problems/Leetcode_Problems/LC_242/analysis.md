# **<span style="color:#ff6b6b">Problem: Valid Anagram</span>**

Given two strings `s` and `t`, determine whether `t` is an **anagram** of `s`.

Definition:

```text
Two strings are anagrams if they contain the same characters
with the same frequencies, possibly in a different order.
```

Example:

```
Input:
s = "anagram"
t = "nagaram"

Output:
True
```

Example:

```
Input:
s = "rat"
t = "car"

Output:
False
```

---

# **<span style="color:#4ecdc4">Analysis of Your Approaches</span>**

You proposed **three approaches**:

1. **Frequency Hash List (Array of size 26)**
2. **Counter (Frequency Dictionary)**
3. **Sorting and Comparison**

These represent **three common interview solutions**, progressing from **optimal → convenient → intuitive**.

---

# **<span style="color:#ffd166">Solution-1: Frequency Hash List</span>**

## **Idea**

Create a **frequency array of size 26** where:

```
index → alphabet
value → frequency of character
```

Example mapping:

```
index 0 → a
index 1 → b
index 2 → c
...
index 25 → z
```

Then:

1. Traverse first string → **increment count**
2. Traverse second string → **decrement count**

If both strings contain the same characters:

```
all values become 0
```

---

# **<span style="color:#a29bfe">Pseudocode</span>**

```
function isAnagram(s, t):

    if length(s) != length(t):
        return False

    create array count[26] filled with 0

    for each character c in s:
        index = c - 'a'
        count[index] += 1

    for each character c in t:
        index = c - 'a'
        count[index] -= 1

    for each value in count:
        if value != 0:
            return False

    return True
```

---

# **<span style="color:#00d2d3">Concept Used</span>**

### **Character Frequency Encoding**

Core principle:

```
Anagrams → identical character counts
```

Example:

```
s = "listen"
t = "silent"
```

Frequency representation:

```
[a,b,c,d,e,f,...]
```

Both produce identical frequency arrays.

Thus:

```
same frequency vector → anagram
```

---

# **<span style="color:#feca57">Pattern Used</span>**

### **Frequency Counting Pattern**

Structure:

```
1. Create frequency structure
2. Update counts
3. Compare counts
```

Frequency structures can be:

```
array
hashmap
counter
```

---

# **<span style="color:#ff9f43">Time Complexity</span>**

Let:

```
n = length of string
```

Traversing both strings:

```
O(n)
```

Checking array:

```
O(26) ≈ O(1)
```

Final complexity:

```
Time = O(n)
```

---

# **<span style="color:#48dbfb">Space Complexity</span>**

Frequency array size:

```
26
```

Constant space.

```
Space = O(1)
```

This is the **most optimal solution**.

---

# **<span style="color:#54a0ff">Solution-2: Counter (Frequency Dictionary)</span>**

## **Idea**

Use Python's **Counter**.

Counter builds a **frequency dictionary** automatically.

Example:

```
Counter("anagram")

{
a:3,
n:1,
g:1,
r:1,
m:1
}
```

Then compare counters.

---

# **<span style="color:#a29bfe">Pseudocode</span>**

```
function isAnagram(s, t):

    if Counter(s) == Counter(t):
        return True
    else:
        return False
```

---

# **<span style="color:#00d2d3">Concept Used</span>**

### **HashMap Frequency Counting**

Structure:

```
key   → character
value → frequency
```

Example:

```
s = "rat"
t = "tar"
```

Both produce:

```
{r:1, a:1, t:1}
```

---

# **<span style="color:#ff9f43">Time Complexity</span>**

Building two counters:

```
O(n)
```

Comparison:

```
O(k)
```

Where `k` = unique characters.

Total:

```
O(n)
```

---

# **<span style="color:#48dbfb">Space Complexity</span>**

Dictionary stores characters.

Worst case:

```
O(n)
```

But usually:

```
O(26)
```

---

# **<span style="color:#f368e0">Solution-3: Sorting and Comparison</span>**

## **Idea**

Sort both strings.

If sorted strings match → anagram.

Example:

```
listen → eilnst
silent → eilnst
```

---

# **<span style="color:#a29bfe">Pseudocode</span>**

```
function isAnagram(s, t):

    sort s
    sort t

    if s == t:
        return True
    else:
        return False
```

---

# **<span style="color:#ff9f43">Time Complexity</span>**

Sorting cost:

```
O(n log n)
```

Comparison:

```
O(n)
```

Total:

```
O(n log n)
```

Slower than frequency approach.

---

# **<span style="color:#48dbfb">Space Complexity</span>**

Sorting may require additional memory.

```
O(n)
```

---

# **<span style="color:#ff6b6b">Rating Your Approaches</span>**

| Approach        | Rating     | Reason                |
| --------------- | ---------- | --------------------- |
| Frequency Array | ⭐⭐⭐⭐⭐ | Optimal solution      |
| Counter         | ⭐⭐⭐⭐   | Clean Python solution |
| Sorting         | ⭐⭐⭐     | Slower                |

### **Overall**

```
9 / 10
```

You correctly identified **the best solution first**, which is excellent.

---

# **<span style="color:#ff9ff3">Other Possible Approaches</span>**

### **Approach: Single HashMap Increment/Decrement**

Instead of two passes:

```
+1 for s
-1 for t
```

Then verify all counts are zero.

This is conceptually similar to your **Solution-1**.

---

# **<span style="color:#00d2d3">LeetCode Problems With Similar Pattern</span>**

### **Anagram / Frequency Pattern**

1. **Valid Anagram**

2. **Group Anagrams**

3. **Find All Anagrams in a String**

4. **Permutation in String**

5. **Ransom Note**

6. **Minimum Window Substring**

7. **Check if Two Strings Are Close**

These all rely on **character frequency tracking**.

---

# **<span style="color:#a29bfe">Practice Questions With Same Pattern</span>**

### **Question-1**

Given two strings, check if they are **permutations of each other**.

---

### **Question-2**

Find **all starting indices of anagrams of `p` in string `s`**.

---

### **Question-3**

Group words with the **same character frequencies**.

---

### **Question-4**

Check if one string can be constructed using characters from another string.

---

### **Question-5**

Find number of **anagram pairs** in a list of strings.

---

# **<span style="color:#00d2d3">Key Pattern Recognition Tip</span>**

Whenever a problem mentions:

```
anagram
permutation
same characters
rearranging letters
```

Immediately think:

```
1. Frequency array
2. HashMap / Counter
3. Sorting
```

This **frequency counting pattern** appears in many **string + sliding window problems** in interviews.
