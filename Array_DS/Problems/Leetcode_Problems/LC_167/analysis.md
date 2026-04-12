
# **<span style="color:#ff6b6b">Problem: Two Sum II – Input Array Is Sorted</span>**

You are given a **sorted array** `numbers` and a `target`.
Return **1-indexed positions** of two numbers such that:

```text
numbers[i] + numbers[j] = target
```

Example:

```text
numbers = [2,7,11,15]
target = 9

Output = [1,2]
```

Because:

```text
2 + 7 = 9
```

---

# **<span style="color:#4ecdc4">Your Solution-1: Pair Enumeration (Brute Force)</span>**

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            p1=numbers[i]
            for j in range(i+1,len(numbers)):
                p2=numbers[j]
                if (p1+p2==target):
                    return [i+1,j+1]
```

---

# **<span style="color:#ffd166">Approach Used</span>**

Pattern:

```text
Pair Enumeration
```

Meaning:

```text
Check every possible pair in the array.
```

Example:

```text
numbers = [2,7,11,15]

Pairs checked:
(2,7)
(2,11)
(2,15)
(7,11)
(7,15)
(11,15)
```

When a pair matches the target → return indices.

---

# **<span style="color:#a29bfe">Pseudocode</span>**

```
for i from 0 → n-1
    for j from i+1 → n-1
        if numbers[i] + numbers[j] == target
            return indices
```

---

# **<span style="color:#00d2d3">Concept Used</span>**

### **Complete Pair Checking**

You generate all combinations of two numbers.

Mathematically:

```text
Total pairs = n(n-1)/2
```

---

# **<span style="color:#feca57">Time Complexity</span>**

Outer loop:

```
n
```

Inner loop:

```
n
```

Total:

```
O(n²)
```

---

# **<span style="color:#ff9f43">Space Complexity</span>**

No extra data structure used.

```
O(1)
```

---

# **<span style="color:#4ecdc4">Your Solution-2: HashMap Approach</span>**

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(numbers)):
            hashmap[numbers[i]]=i
        for i in range(len(numbers)):
            if (target-numbers[i] in hashmap):
                return [i+1,hashmap.get(target-numbers[i])+1]
```

---

# **<span style="color:#ffd166">Approach Used</span>**

Pattern:

```text
HashMap Complement Search
```

Key idea:

```
a + b = target
```

Rewrite:

```
b = target - a
```

So for each number we check:

```
does complement exist?
```

---

# **<span style="color:#a29bfe">Pseudocode</span>**

```
create hashmap

for each number
    store number → index

for each number
    complement = target - number
    if complement exists
        return indices
```

---

# **<span style="color:#ff6b6b">Critical Issue in Your Code</span>**

Your solution may return the **same element twice**.

Example:

```
numbers = [3,3]
target = 6
```

Hashmap:

```
{3:1}
```

Iteration:

```
i=1
target-numbers[i] = 3
```

It returns:

```
[2,2]
```

But correct answer should be:

```
[1,2]
```

Because **same element cannot be reused**.

---

# **<span style="color:#00d2d3">Correct HashMap Solution</span>**

Better version:

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}

        for i,num in enumerate(numbers):

            complement = target - num

            if complement in hashmap:
                return [hashmap[complement]+1, i+1]

            hashmap[num]=i
```

This ensures:

```
we never reuse the same index
```

---

# **<span style="color:#48dbfb">Time Complexity</span>**

Loop:

```
O(n)
```

Hashmap lookup:

```
O(1)
```

Total:

```
O(n)
```

---

# **<span style="color:#1dd1a1">Space Complexity</span>**

Hashmap stores elements.

```
O(n)
```

---

# **<span style="color:#54a0ff">Best Solution (Because Array Is Sorted)</span>**

Since the array is **already sorted**, the best pattern is:

```
Two Pointer
```

---

# **<span style="color:#ffd166">Two Pointer Idea</span>**

Start with:

```
left = smallest element
right = largest element
```

If sum is too large → move right pointer.

If sum is too small → move left pointer.

---

# **<span style="color:#a29bfe">Two Pointer Code</span>**

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers)-1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left+1,right+1]

            elif current_sum < target:
                left += 1

            else:
                right -= 1
```

---

# **<span style="color:#feca57">Complexity of Best Solution</span>**

Time:

```
O(n)
```

Space:

```
O(1)
```

Better than hashmap because:

```
no extra memory
```

---

# **<span style="color:#ff6b6b">Rating Your Approaches</span>**

| Approach           | Rating |
| ------------------ | ------ |
| Pair Enumeration   | ⭐⭐⭐    |
| HashMap            | ⭐⭐⭐⭐   |
| Two Pointer (Best) | ⭐⭐⭐⭐⭐  |

Overall reasoning:

```
8.5 / 10
```

You correctly recognized:

* **pair enumeration**
* **hashmap complement pattern**

Good pattern recognition.

---

# **<span style="color:#f368e0">LeetCode Problems With Same Pattern</span>**

### **Complement HashMap Pattern**

1. Two Sum
2. Subarray Sum Equals K
3. 3Sum
4. 4Sum
5. Contains Duplicate
6. Longest Substring Without Repeating Characters

---

### **Two Pointer Pattern**

1. Two Sum II
2. Container With Most Water
3. 3Sum
4. Remove Duplicates from Sorted Array
5. Valid Palindrome

---

# **<span style="color:#00d2d3">Practice Questions With Same Pattern</span>**

### Question 1

Find **two numbers whose difference equals k**.

---

### Question 2

Find **three numbers whose sum equals target**.

---

### Question 3

Find **all pairs whose sum is smaller than target**.

---

### Question 4

Find **two numbers whose product equals target**.

---

### Question 5

Count number of pairs with sum equal to target.

---

If you'd like, I can also show you something **extremely useful for interviews**:

**How the Two Pointer pattern solves ~25 different array problems using the same template.**
