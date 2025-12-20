## **1️⃣ What is `Counter`?**

- `Counter` is a **subclass of `dict`** specialized for counting **hashable items**.
- It **maps elements to their frequency counts**.
- Example:

```python
from collections import Counter

s = "anagram"
count = Counter(s)
print(count)
```

**Output:**

```
Counter({'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})
```

✅ Explanation:

- `'a'` occurs 3 times → `'a': 3`
- Other letters occur once.
- Works with **strings, lists, tuples, etc.**

---

## **2️⃣ How `Counter` works internally**

1. `Counter` stores **items as keys** in a dictionary.
2. Each **key maps to a count** (the value).
3. When you initialize with an iterable, it **iterates once over all elements**, updating the count:

```python
count = {}
for element in iterable:
    count[element] = count.get(element, 0) + 1
```

- So, **time complexity = O(n)**, where n = length of iterable.
- Space complexity = O(k), where k = number of unique elements.

---

## **3️⃣ Common Operations**

### **a) Access count**

```python
count['a']    # 3
count['z']    # 0 (does not throw error)
```

### **b) Compare two Counters**

```python
s = "anagram"
t = "nagaram"
Counter(s) == Counter(t)   # True → they have same frequencies
```

### **c) Most common elements**

```python
count.most_common(2)   # [('a', 3), ('n', 1)]
```

### **d) Increment / Decrement counts**

```python
count['a'] += 1
count['b'] -= 1
```

---

## **4️⃣ Why `Counter` is efficient for anagrams**

- Counting frequency of letters → O(n)
- Comparing two Counters → O(k) (number of unique letters)
- Handles **any characters**, not just a-z

So your **anagram check**:

```python
return Counter(s) == Counter(t)
```

- Counts letters in `s` → O(n)
- Counts letters in `t` → O(n)
- Compare dictionaries → O(k)
  ✅ Total = **O(n)** time, **O(k)** space

---

### **5️⃣ Visualization**

If `s = "apple"`:

| Letter | Count |
| ------ | ----- |
| a      | 1     |
| p      | 2     |
| l      | 1     |
| e      | 1     |

`Counter` stores it as a dict:

```python
{'a':1, 'p':2, 'l':1, 'e':1}
```

When comparing two Counters:

- Python internally compares **keys and values**
- If all match → returns `True`

---

✅ **Summary**

- `Counter` = frequency map (dict subclass)
- O(n) to build from iterable
- Supports arithmetic, comparison, and most_common queries
- Perfect for problems like: **anagrams, frequency counting, top-k elements**

---
