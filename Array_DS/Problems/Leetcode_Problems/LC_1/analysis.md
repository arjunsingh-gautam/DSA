# **<span style="color:#ff6b6b">Problem: Two Sum</span>**

Given an array `nums` and a target value `target`, return the **indices of two numbers** such that:

```text
nums[i] + nums[j] = target
```

Example:

```
nums = [2,7,11,15]
target = 9

Output: [0,1]
```

Because:

```
2 + 7 = 9
```

---

# **<span style="color:#4ecdc4">Your Approaches</span>**

You proposed **two approaches**:

1️⃣ **Brute Force — Pair Enumeration**
2️⃣ **Optimized — HashMap Lookup**

Both are correct and follow the standard **interview progression**.

---

# **<span style="color:#ffd166">Solution-1: Brute Force Approach</span>**

## **<span style="color:#feca57">Idea</span>**

Check **every possible pair** in the array and see if their sum equals the target.

Example:

```
nums = [1,2,5]
target = 7

Pairs checked:
(1,2)
(1,5)
(2,5)
```

If any pair sum equals the target → return indices.

---

# **<span style="color:#a29bfe">Pseudocode</span>**

```
function twoSum(nums, target):

    for i from 0 to n-1:
        for j from i+1 to n-1:

            if nums[i] + nums[j] == target:
                return [i, j]
```

---

# **<span style="color:#00d2d3">Concept Used</span>**

### **Pair Enumeration**

This concept means:

```
Check all combinations of two elements
```

Formula:

```
Total pairs = n(n-1)/2
```

This is why complexity becomes **quadratic**.

---

# **<span style="color:#ff9f43">Time Complexity</span>**

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

# **<span style="color:#48dbfb">Space Complexity</span>**

No extra data structure used.

```
Space = O(1)
```

---

# **<span style="color:#1dd1a1">Strengths</span>**

✔ Very simple
✔ Easy to implement
✔ Works for all cases

---

# **<span style="color:#ff6b6b">Weakness</span>**

Very slow for large input.

Example:

```
n = 10^5
```

Operations:

```
10^10
```

Too slow.

---

# **<span style="color:#54a0ff">Solution-2: Optimized Approach</span>**

### **Pattern: HashMap Lookup**

Your idea:

```
Store visited numbers in hashmap
```

Key:

```
number
```

Value:

```
index
```

Instead of searching the whole array again, we check **complement**.

Complement formula:

```
complement = target - nums[i]
```

---

# **<span style="color:#f368e0">Pseudocode</span>**

```
function twoSum(nums, target):

    create empty hashmap

    for i from 0 to n-1:

        complement = target - nums[i]

        if complement exists in hashmap:
            return [hashmap[complement], i]

        store nums[i] in hashmap with index i
```

---

# **<span style="color:#ff9ff3">Example Walkthrough</span>**

```
nums = [2,7,11,15]
target = 9
```

Step-1:

```
i = 0
nums[i] = 2
complement = 7
hashmap = {2:0}
```

Step-2:

```
i = 1
nums[i] = 7
complement = 2
```

2 exists in hashmap → solution found.

```
return [0,1]
```

---

# **<span style="color:#feca57">Concept Used</span>**

### **Hashing + Complement Search**

Key insight:

Instead of solving:

```
a + b = target
```

We rewrite as:

```
b = target - a
```

So for each element we **search complement**.

Hashmap allows:

```
O(1) lookup
```

---

# **<span style="color:#ff9f43">Pattern Used</span>**

### **Complement Lookup Pattern**

Steps:

```
1. Iterate array
2. Compute complement
3. Check hashmap
4. Insert current element
```

This pattern is extremely common in interviews.

---

# **<span style="color:#48dbfb">Time Complexity</span>**

Loop runs:

```
n
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

Hashmap stores at most `n` elements.

```
Space = O(n)
```

---

# **<span style="color:#ff6b6b">Rating Your Approach</span>**

| Criteria                       | Rating     |
| ------------------------------ | ---------- |
| Understanding                  | ⭐⭐⭐⭐⭐ |
| Correct pattern identification | ⭐⭐⭐⭐⭐ |
| Time complexity awareness      | ⭐⭐⭐⭐⭐ |
| Explanation clarity            | ⭐⭐⭐⭐   |

### **Overall Rating**

```
9 / 10
```

Your thinking process is **exactly how interviewers expect candidates to reason**.

---

# **<span style="color:#54a0ff">Other Possible Approaches</span>**

## **Approach 3 — Sorting + Two Pointers**

Steps:

```
1. Sort array
2. Use left pointer
3. Use right pointer
4. Move pointers depending on sum
```

Example:

```
nums = [2,7,11,15]
target = 9
```

```
left = 2
right = 15
```

But problem:

```
Sorting destroys original indices
```

Requires extra tracking.

---

# **<span style="color:#f368e0">LeetCode Problems With Same Pattern</span>**

These use **HashMap Complement Pattern**.

1️⃣ **Two Sum**

2️⃣ **Two Sum II – Input Sorted Array**

3️⃣ **3Sum**

4️⃣ **4Sum**

5️⃣ **Subarray Sum Equals K**

6️⃣ **Contains Duplicate**

7️⃣ **Longest Substring Without Repeating Characters**

---

# **<span style="color:#00d2d3">Problems With Similar Thinking Pattern</span>**

### **Question-1**

Given array and target, return **number of pairs whose sum = target**.

---

### **Question-2**

Find **two numbers whose difference = k**.

---

### **Question-3**

Find **three numbers whose sum = target**.

---

### **Question-4**

Check if array contains **duplicate values**.

---

### **Question-5**

Return **indices of two numbers whose product = target**.

---

# **<span style="color:#a29bfe">Important Interview Insight</span>**

Whenever you see:

```
Find two numbers whose sum = target
```

Immediately think:

```
Complement = target - current_element
```

Then choose:

```
HashMap
OR
Two pointers (if sorted)
```

This is one of the **most important DSA patterns**.

---

If you want, I can also show you:

**The 7 core patterns hidden inside Two Sum that appear in 100+ interview problems.**
